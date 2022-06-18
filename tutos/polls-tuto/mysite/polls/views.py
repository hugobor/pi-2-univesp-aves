from django.shortcuts import render, reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from django.db.models import F

from .models import Question, Choice




def index( request ):
    QUESTIONS = 6
    
    latest_question_list = Question.objects.order_by( '-pub_date' )[: QUESTIONS]
    output = ', '.join( map( lambda q: q.question_text, latest_question_list ))
    context = {
        'latest_question_list': latest_question_list,
    }
    return render( request, 'polls/index.html', context )



def detail( request, question_id ):
    question = get_object_or_404( Question, pk = question_id )
    return render( request, 'polls/detail.html', { 'question': question } )



def results( request, question_id ):
    question = get_object_or_404( Question, pk = question_id )
    return render( request, 'polls/results.html', { 'question': question })



def vote( request, question_id ):
    question = get_object_or_404( Question, pk = question_id )

    try:
        selected_choice = question.choice_set.get( pk = request.POST[ 'choice' ])
    except (KeyError, Choice.DoesNotExist ):
        return render( request, 'polls/detail.html',
                       { 'question': question,
                         'error_message': "Escolha uma resposta." })
    else:
        selected_choice.votes = F( 'votes' ) + 1
        selected_choice.save()

        return HttpResponseRedirect( reverse( 'polls:results', args = ( question.id, )))

from django.test import TestCase

from django.utils import timezone
from django.urls import reverse

from .models import Question

import datetime


def create_question( question_text, days ):
    time = timezone.now() + datetime.timedelta( days = days )
    return Question.objects.create( question_text = question_text, pub_date = time )



class QuestionModelTests( TestCase ):

    def test_was_published_recently_future_question( self ):
        future_time = timezone.now() + datetime.timedelta( days=69 )
        future_question = Question( pub_date = future_time )

        self.assertIs( future_question.was_published_recently(), False )


    def text_was_published_recently_with_old_question( self ):
        time = timezone.now() - datetime.timedelta( days = 1, seconds = 1 )
        old_question = Question( pub_date = time )

        self.assertIs( old_question.was_published_recently(), False )

        
    def text_was_published_recently_with_recent_question( self ):
        time = timezone.now() - datetime.timedelta( hours=23, minutes=59, seconds=59 )
        recent_question = Question( pub_date = time )

        self.assertIs( recent_question.was_published_recently(), True )
        

class QuestionIndexViewTests( TestCase ):

    def test_no_questions( self ):
        response = self.client.get( reverse( 'polls:index' ))
        self.assertEqual( response.status_code, 200 )
        self.assertContains( response, "Sem votações" )


    def test_past_questions( self ):
        question = create_question( "Questão no futuro...", 12 )
        response = self.client.get( reverse( 'polls:index' ))
        self.assertContains( response, "Sem votações" )
        self.assertQuerysetEqual( response.context[ 'latest_question_list' ], [] )

    def test_future_and_past_questions( self ):
        future_question = create_question( "Questão no futuro...", 3 )
        past_question = create_question( "Questão no passado...", -2 )        
        response = self.client.get( reverse( 'polls:index' ))
        self.assertQuerysetEqual( response.context[ 'latest_question_list' ],
                                  [past_question] )

    def test_three_past_questions( self ):
        q1 = create_question( "Questão no futuro...", 12 )
        q2 = create_question( "AAAAAAAAAAAAAAA", -1 )
        q3 = create_question( "Bilobinha", -3 )

        response = self.client.get( reverse( 'polls:index' ))
        self.assertQuerysetEqual( response.context[ 'latest_question_list' ],
                                  [ q2, q3 ])
        

class QuestionDetailViewTests( TestCase ):
    def test_future_question( self ):
        future_question = create_question( "Pergunta no futuro!!!!", 3 )
        response = self.client.get( reverse( 'polls:detail', args = ( future_question.id ,)))
        self.assertEqual( response.status_code, 404 )

    def test_past_question( self ):
        past_question = create_question( "Pregunta no passado...", -2 )
        response = self.client.get( reverse( 'polls:detail', args = ( past_question.id ,)))
        self.assertContains( response, past_question.question_text )


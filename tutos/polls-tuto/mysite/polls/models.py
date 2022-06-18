import datetime

from django.db import models
from django.utils import timezone


class Question( models.Model ):
    question_text = models.TextField( 'pergunta' )
    pub_date = models.DateTimeField( 'data de publicação', default = timezone.now )

    def __str__( self ):
        return self.question_text

    def was_published_recently( self, days = 1 ):
        return self.pub_date >= timezone.now() - datetime.timedelta( days = days )


class Choice( models.Model ):
    question = models.ForeignKey( Question, on_delete = models.CASCADE )
    choice_text = models.TextField( 'resposta' )
    votes = models.PositiveIntegerField( 'votos', default = 0 )

    def __str__( self ):
        return self.choice_text

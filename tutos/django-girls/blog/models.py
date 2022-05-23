from django.db import models
from django.conf import settings
from django.utils import timezone

# Olá!!!! 🙋

class Post( models.Model ):
    """Postagem no blog!!!!!! :O"""

    author = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete = models.CASCADE )
    title = models.CharField( max_length = 550 )
    text = models.TextField()
    creation_date = models.DateTimeField( default = timezone.now )
    published_date = models.DateTimeField( blank = True, null = True )


    def publish( self ):
        """Publica (salva) postagem. :|"""
        self.published_date = timezone.now()
        self.save()

    def __str__( self ):
        return self.title
    

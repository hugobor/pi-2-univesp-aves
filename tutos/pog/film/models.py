from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Genero( models.Model ):
    nome = models.CharField( max_length = 1000 )

    def __str__( self ):
        return self.nome


class Filme( models.Model ):
    titulo = models.TextField( 'título', blank = True )
    descricao = models.TextField( 'descrição', blank = True )
    ano = models.PositiveIntegerField( blank = True, null = True )
    genero = models.ForeignKey( Genero, blank = True, null = True, on_delete = models.CASCADE )

    def __str__( self ):
        return self.titulo

    
        

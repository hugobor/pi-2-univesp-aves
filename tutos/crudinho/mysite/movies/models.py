from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

BIG_CHARFIELD = 2048


class Genre( models.Model ):
    name = models.CharField( verbose_name = 'nome',
                             max_length = BIG_CHARFIELD )

    def __str__( self ):
        return self.name


class Film( models.Model ):
    title = models.CharField( verbose_name = 'título',
                              max_length = BIG_CHARFIELD )
    length = models.PositiveIntegerField( verbose_name = 'duração',
                                          blank = True,
                                          null = True )
    year = models.PositiveIntegerField( verbose_name = 'ano',
                                        blank = True,
                                        null = True )
    score = models.FloatField( verbose_name = 'nota',
                               blank = True,
                               null = True,
                               validators = [ MinValueValidator( 0 ),
                                              MaxValueValidator( 5 ) ])
    genre = models.ForeignKey( Genre,
                               verbose_name = 'gênero',
                               blank = True,
                               null = True,
                               on_delete = models.CASCADE )

    def __str__( self ):
        if self.year:
            return f"{self.title} ({self.year})"
        else:
            return self.title



class Console( models.Model ):
    nome = models.CharField( max_length = BIG_CHARFIELD, unique = True )

    def __str__( self ):
        return self.nome

    class Meta:
        ordering = [ 'nome' ]
        

class Gamu( models.Model ):
    nome = models.CharField( max_length = BIG_CHARFIELD, db_index = True )
    descricao = models.TextField( default = '' )
    capa = models.ImageField()
    nota = models.PositiveIntegerField( null = True,
                                        validators = [ MinValueValidator( 0 ),
                                                       MaxValueValidator( 5 )])
    console = models.ForeignKey( to = Console, on_delete = models.CASCADE )

    def __str__( self ):
        return self.nome

    class Meta:
        ordering = [ 'nome' ]
    
                             

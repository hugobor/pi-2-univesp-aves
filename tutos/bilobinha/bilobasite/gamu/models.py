from django.db import models

BIG_CHARFIELD = 2048

class Console( models.Model ):
    nome = models.CharField( max_length = BIG_CHARFIELD, db_index = True )
    imagem = models.ImageField( null = True, blank = True )

    class Meta:
        ordering = [ 'nome' ]

    def __str__( self ):
        return self.nome


class TableLinesMixin():
    table_lines_default = []

    def table_fields( self ):
        return [ self._meta.get_field( fname ) for fname in self.table_lines_default ]
    
    def table_headers( self ):
        return [ field.verbose_name.title() for field in self.table_fields() ]

    def table_line( self ):
        return [ field.value_from_object( self ) for field in self.table_fields() ]

    def as_dict( self ):
        fields = self.table_fields()
        return { field.verbose_name.title(): field.value_from_object( self )
                 for field in fields }
                 
    
    
    
class Game( models.Model, TableLinesMixin ):
    nome = models.CharField( max_length = BIG_CHARFIELD, db_index = True )
    imagem_capa = models.ImageField( 'Imagem de Capa', null = True, blank = True )
    descricao = models.TextField( 'descrição', blank = True )
    ano = models.PositiveIntegerField( 'ano de lançamento' )
    console = models.ForeignKey( Console, on_delete = models.CASCADE )

    class Meta:
        ordering = [ 'nome' ]

    def __str__( self ):
        return f"{self.nome} ({self.ano})"

    table_lines_default = [ 'nome', 'ano', 'console', 'imagem_capa' ]

    def get_absolute_url( self ):
        """Se eu redefinir isso as views de edição redirecional altomaticamente sem usar o success_url"""
        return f"/game/{self.id}/detail/"




class DescricaoExtra( models.Model ):
    game = models.ForeignKey( Game, on_delete = models.CASCADE )
    titulo = models.CharField( 'título', max_length = BIG_CHARFIELD )
    texto = models.TextField( blank = True )
    
    class Meta:
        verbose_name = 'descrição extra'

    def __str__( self ):
        return f"{self.game.nome}: {self.titulo}"

    
class ScreenShot( models.Model ):
    game = models.ForeignKey( Game, on_delete = models.CASCADE )
    imagem = models.ImageField()
    legenda = models.CharField( max_length = BIG_CHARFIELD, blank = True, null = True, default = None )

    def __str__( self ):
        return f"Screenshot #{self.pk}, game: {self.game.nome}"

from django.db import models

from django.db.models.signals import pre_save
from django.dispatch import receiver


_BigCharField = 2048 #para não ter que configurar o tamanho de tudo


class Ave( models.Model ):
    """Modelo de Aves."""
    
    nome_cientifico = models.CharField( 'nome científico',
                                        max_length = _BigCharField,
                                        unique = True )

    autor = models.CharField( 'nome do autor',
                              max_length = _BigCharField,
                              null = True,
                              blank = True )
    nome_popular = models.CharField( 'nome popular',
                                     max_length = _BigCharField,
                                     null = True,
                                     blank = True )
    nome_ingles = models.CharField( 'nome em inglês',
                                    max_length = _BigCharField,
                                    blank = True,
                                    null = True )

    familia = models.ForeignKey( 'familia',
                                 verbose_name = 'família',
                                 on_delete = models.SET_NULL,
                                 null = True,
                                 blank = True )

    frequencia_ocorrencia = models.IntegerField( 'frequência de ocorrência',
                                                 null = True,
                                                 blank = True )
    abundancia_relativa = models.CharField( 'abundância relativa',
                                            max_length = 2,
                                            null = True,
                                            blank = True )    
    
    ESTADOS_CONSERVACAO = (
        ( 'LC', 'Pouco Preocupante' ),
        ( 'NT', 'Quase Ameaçada' ),
        ( 'VU', 'Vulnerável' ),
        ( 'EN', 'Em Perigo' ),
        ( 'CR', 'Criticamente em Perigo' ),
        ( 'EW', 'Extinta na Natureza', ),
        ( 'EX', 'Extinta' ),
        ( 'DD', 'Dados Insuficientes', ),
        ( 'NE', 'Não Avaliada', ),
    )

    ESTADOS_CONSERVACAO_EN = (
        ( 'LC', 'Least Concern', 'aves/static/iucn/LC.png' ),
        ( 'NT', 'Near Threatened', 'aves/static/iucn/NT.png' ),
        ( 'VU', 'Vulnerable', 'aves/static/iucn/VU.png' ),
        ( 'EN', 'Endangered', 'aves/static/iucn/EN.png' ),
        ( 'CR', 'Critically Endangered', 'aves/static/iucn/CR.png' ),
        ( 'EW', 'Extinct in The Wild', 'aves/static/iucn/EW.png' ),
        ( 'EX', 'Extinct', 'aves/static/iucn/EX.png' ),
        ( 'DD', 'Data Deficient', 'aves/static/iucn/DD.png' ),
        ( 'NE', 'Not Evaluated', 'aves/static/iucn/NE.png' ),
    )

    ESTADOS_CONSERVACAO_IMG = (
        ( 'LC', 'aves/iucn/LC.png' ),
        ( 'NT', 'aves/iucn/NT.png' ),
        ( 'VU', 'aves/iucn/VU.png' ),
        ( 'EN', 'aves/EN.png' ),
        ( 'CR', 'aves/iucn/CR.png' ),
        ( 'EW', 'aves/iucn/EW.png' ),
        ( 'EX', 'aves/iucn/EX.png' ),
        ( 'DD', 'aves/iucn/DD.png' ),
        ( 'NE', 'aves/iucn/NE.png' ),
    )

    estado_iucn_sp = models.CharField( 'estado de conservação em São Paulo',
                                       max_length = 2,
                                       choices = ESTADOS_CONSERVACAO,
                                       null = True,
                                       blank = True )

    estado_iucn_int = models.CharField( 'estado de conservação Internacional',
                                        max_length = 2,
                                        choices = ESTADOS_CONSERVACAO,
                                        null = True,
                                        blank = True )

    info = models.TextField( 'informações gerais', blank = True )
    
    imagem_capa = models.ImageField( 'imagem de capa', null = True, blank = True )


    def __str__( self ):
        return self.nome_especie()

    
    def nome_especie( self ):
        """Retorna o nome 'Subfamília Espécie' como 'S. espécie'.
        Se tiver menos de duas palavras no nome retorna o nome como title"""
        spli = self.nome_cientifico.lower().split()
        if len( spli ) < 2:
            return self.nome_cientifico.strip().title()
        else:
            spli[ 0 ] = spli[ 0 ][ :1 ].title() + '.'
            return ' '.join( spli )

    

    class Meta:
        ordering = [ 'nome_cientifico' ]



@receiver( pre_save, sender = Ave )
def create_ave( sender, instance, *args, **kwargs ):
    """Arruma os campos antes de salvar."""
    instance.nome_cientifico = instance.nome_cientifico.capitalize()


    
        
class InfoExtra( models.Model ):
    """Capos extras com informações de texto de aves.
    Exemplo: Alimentação, reprodução, sub-espécies, habitos...
    Modelo Ave tem um campo de informações gerais."""
    
    ave = models.ForeignKey( Ave, on_delete = models.CASCADE )
    titulo = models.CharField( 'título', max_length = _BigCharField )
    texto = models.TextField()

    class Meta:
        verbose_name = 'informação extra'
        verbose_name_plural = 'informações extras'

    def __str__( self ):
        return f"{self.ave.nome_cientifico}: {self.titulo}"


class FotoAve( models.Model ):
    """Fotos extras para as aves.
    Modelo Ave tem um campo para imagem de capa."""
    
    ave = models.ForeignKey( Ave, on_delete = models.CASCADE )
    imagem = models.ImageField()
    leganda = models.CharField( max_length = _BigCharField, blank = True )
        
    def __str__( self ):
        return f"Foto #{self.id} de {self.ave.nome_cientifico}"

    class Meta:
        verbose_name = "foto de ave"
        verbose_name_plural = "fotos de aves"

        

class ClassifiExtra( models.Model ):
    """Campos extras para classificação de taxonomia."""
    reino = models.CharField( max_length = _BigCharField,
                              blank = True,
                              null = True )
    filo = models.CharField( max_length = _BigCharField,
                                    blank = True,
                                    null = True )
    classe = models.CharField( max_length = _BigCharField )

    class Meta:
        ordering = [ 'classe' ]
        verbose_name = 'classificação extra'
        verbose_name_plural = 'classificações estras'

    def __str__( self ):
        def nod( s ):
            """Name or dash."""
            return s if s != '' else '---'
        
        return f"Classe: {nod(self.classe)}; Filo: {nod(self.filo)}; Reino: {nod(self.reino)}"

        
class Ordem( models.Model ):
    classifiextra = models.ForeignKey( ClassifiExtra,
                                       verbose_name = 'classificação extra',
                                       null = True,
                                       blank = True,
                                       on_delete = models.SET_NULL )
    
    nome = models.CharField( max_length = _BigCharField, unique = True )

    class Meta:
        verbose_name_plural = 'ordens'
        ordering = [ 'nome' ]

    def __str__( self ):
        return self.nome.title()


class Familia( models.Model ):
    ordem = models.ForeignKey( Ordem, on_delete = models.CASCADE )
    
    nome = models.CharField( max_length = _BigCharField, unique = True )
    autor = models.CharField( max_length = _BigCharField, null = True, blank = True )

    class Meta:
        verbose_name = 'família'
        ordering = [ 'nome' ]

    def __str__( self ):
        return self.nome.title()
    
   

                                      
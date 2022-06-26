from django.db import models


_BigCharField = 2048 #para não ter que configurar o tamanho de tudo


class Ave( models.Model ):
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
    abundancia_relativa = models.IntegerField( 'abundância relativa',
                                               null = True,
                                               blank = True)    
    
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


class InfoExtra( models.Model ):
    ave = models.ForeignKey( Ave, on_delete = models.CASCADE )
    titulo = models.CharField( 'título', max_length = _BigCharField )
    texto = models.TextField()

    class Meta:
        verbose_name = 'informação extra'
        verbose_name_plural = 'informações extras'

    def __str__( self ):
        return f"{self.ave.nome_cientifico}: {self.titulo}"


class FotoAve( models.Model ):
    ave = models.ForeignKey( Ave, on_delete = models.CASCADE )
    imagem = models.ImageField()
    leganda = models.CharField( max_length = _BigCharField, blank = True )
        
    def __str__( self ):
        return f"Foto #{self.id} de {self.ave.nome_cientifico}"

    class Meta:
        verbose_name = "foto de ave"
        verbose_name_plural = "fotos de aves"

        
class Ordem( models.Model ):
    nome = models.CharField( max_length = _BigCharField, unique = True )

    class Meta:
        verbose_name_plural = 'ordens'
        ordering = [ 'nome' ]

    def __str__( self ):
        return self.nome.title()


class Familia( models.Model ):
    ordem = models.ForeignKey( Ordem, on_delete = models.CASCADE )
    nome = models.CharField( max_length = _BigCharField, unique = True )

    class Meta:
        verbose_name = 'família'
        ordering = [ 'nome' ]

    def __str__( self ):
        return self.nome.title()
    
   

                                      

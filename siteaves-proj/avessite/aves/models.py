from django.db import models


_BigCharField = 2048 #para não ter que configurar o tamanho de tudo

class Ave( models.Model ):
    nome_cientifico = models.CharField( 'nome científico',
                                        max_length = _BigCharField,
                                        unique = True )
    nome_popular = models.CharField( 'nome popular',
                                     max_length = _BigCharField,
                                     blank = True,
                                     null = True )
    nome_ingles = models.CharField( 'nome em inglês',
                                    max_length = _BigCharField,
                                    blank = True,
                                    null = True )
    
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
        ( 'LC', 'Least Concern', '/static/iucn/LC.png' ),
        ( 'NT', 'Near Threatened', '/static/iucn/NT.png' ),
        ( 'VU', 'Vulnerable', '/static/iucn/VU.png' ),
        ( 'EN', 'Endangered', '/static/iucn/EN.png' ),
        ( 'CR', 'Critically Endangered', '/static/iucn/CR.png' ),
        ( 'EW', 'Extinct in The Wild', '/static/iucn/EW.png' ),
        ( 'EX', 'Extinct', '/static/iucn/EX.png' ),
        ( 'DD', 'Data Deficient', '/static/iucn/DD.png' ),
        ( 'NE', 'Not Evaluated', '/static/iucn/NE.png' ),
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
                                       null = True )

    descricao = models.TextField( blank = True )
    
    imagem_capa = models.ImageField( null = True )


    def __str__( self ):
        return self.nome_cientifico


    class Meta:
        ordering = [ 'nome_cientifico' ]
   

                                      

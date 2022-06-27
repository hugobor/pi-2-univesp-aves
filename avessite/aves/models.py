from django.db import models

from django.db.models.signals import pre_save
from django.dispatch import receiver


_BigCharField = 2048 #para não ter que configurar o tamanho de tudo


def pick_val_in_choice( choice_tpl, choice_val ):
    """Gambiara para pegar valor em lista de tupla de choice."""
    choice_val = choice_val.strip().casefold()
    for key, val in choice_tpl:
        if key.casefold() == choice_val:
            return val

    return None


def choice_from_display_name( choice_tpl, search_display ):
    """Gambiarra para pegar as escolhas pelo nome de display"""
    search_display = search_display.strip().casefold()
    rev = [ ( display_name.strip().casefold(), choice )
            for choice, display_name
            in choice_tpl ]
    return pick_val_in_choice( rev, search_display )


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
        ( 'LC', 'Least Concern' ),
        ( 'NT', 'Near Threatened' ),
        ( 'VU', 'Vulnerable' ),
        ( 'EN', 'Endangered' ),
        ( 'CR', 'Critically Endangered' ),
        ( 'EW', 'Extinct in The Wild' ),
        ( 'EX', 'Extinct' ),
        ( 'DD', 'Data Deficient' ),
        ( 'NE', 'Not Evaluated' ),
    )

    ESTADOS_CONSERVACAO_IMG = (
        ( 'LC', 'aves/iucn/LC.png' ),
        ( 'NT', 'aves/iucn/NT.png' ),
        ( 'VU', 'aves/iucn/VU.png' ),
        ( 'EN', 'aves/iucn/EN.png' ),
        ( 'CR', 'aves/iucn/CR.png' ),
        ( 'EW', 'aves/iucn/EW.png' ),
        ( 'EX', 'aves/iucn/EX.png' ),
        ( 'DD', 'aves/iucn/DD.png' ),
        ( 'NE', 'aves/iucn/NE.png' ),
    )    

    def pick_iucn_sp_img( self ):
        """Pega o caminho para a imagem do estado de conservação..."""
        return pick_val_in_choice( self.ESTADOS_CONSERVACAO_IMG, self.estado_iucn_sp )

    def pick_iucn_int_img( self ):
        """Pega o caminho para a imagem do estado de conservação..."""
        return pick_val_in_choice( self.ESTADOS_CONSERVACAO_IMG, self.estado_iucn_int )

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
        return self.nome_cientifico

    
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

    def familia_count( self ):
        """Conta quantidade total de famílias nas ordens."""
        s = 0
        for ordem in self.ordem_set.all():
            s += ordem.familia_set.count()
        return s
    

        
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
    
   

                                      

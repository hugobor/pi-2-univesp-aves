from django.test import TestCase
from django.urls import reverse

from http import HTTPStatus

from .models import Ave, Ordem, Familia, ClassifiExtra

from .models import pick_val_in_choice, choice_from_display_name

BLAPU_TEST = (
    ('MA', 'Mandioca' ),
    ('CE', 'Cebola' ),
    ('LH', 'Coelho' ),
    ('MC', 'Maçã' ),
)

class ModelUtilsTest( TestCase ):
    """Testa as funçõezinhas de utilidade..."""

    def test_pick_val_in_choice( self ):
        self.assertIs( pick_val_in_choice( BLAPU_TEST, 'MA' ), 'Mandioca' )
        self.assertIs( pick_val_in_choice( BLAPU_TEST, 'MC' ), 'Maçã' )
        self.assertIs( pick_val_in_choice( BLAPU_TEST, 'OI' ), None )
        self.assertIs( pick_val_in_choice( BLAPU_TEST, 'oi' ), None )
        self.assertIs( pick_val_in_choice( BLAPU_TEST, '' ), None )
        self.assertIs( pick_val_in_choice( (), '' ), None )
        self.assertIs( pick_val_in_choice( (), 'dsafkçladsçklf' ), None )
        self.assertIs( pick_val_in_choice( BLAPU_TEST, 'ma' ), 'Mandioca' )
        self.assertIs( pick_val_in_choice( BLAPU_TEST, 'lH' ), 'Coelho' )
        self.assertIs( pick_val_in_choice( BLAPU_TEST, '  lH  ' ), 'Coelho' )

    def test_choice_from_display_name( self ):
        self.assertIs( choice_from_display_name( BLAPU_TEST, 'MA' ), None )
        self.assertIs( choice_from_display_name( BLAPU_TEST, 'mandioca' ), 'MA' )
        self.assertIs( choice_from_display_name( BLAPU_TEST, 'Mandioca' ), 'MA' )
        self.assertIs( choice_from_display_name( BLAPU_TEST, '   MandiocA   ' ), 'MA' )
        self.assertIs( choice_from_display_name( BLAPU_TEST, 'afsdflasdo' ), None )
        self.assertIs( choice_from_display_name( BLAPU_TEST, 'maçã' ), 'MC' )        

    

class AveTest( TestCase ):
    def test_nome_especie( self ):
        a = Ave.objects.create( nome_cientifico = 'Bilobinho' )
        b = Ave.objects.create( nome_cientifico = 'Bilobinho Amolinho' )
        c = Ave.objects.create( nome_cientifico = 'Bilobinho Amolinho Chumbolino' )
        d = Ave.objects.create( nome_cientifico = 'B. Amolinho' )
        e = Ave.objects.create( nome_cientifico = 'animaniaco' )

        self.assertEqual( a.nome_especie(), 'Bilobinho' )
        self.assertEqual( b.nome_especie(), 'B. amolinho' )
        self.assertEqual( c.nome_especie(), 'B. amolinho chumbolino' )
        self.assertEqual( d.nome_especie(), 'B. amolinho' )
        self.assertEqual( e.nome_especie(), 'Animaniaco' )        

    def test_subfamilia( self ):
        a = Ave.objects.create( nome_cientifico = 'Bilobinho' )
        b = Ave.objects.create( nome_cientifico = 'Bilobinho Amolinho' )
        c = Ave.objects.create( nome_cientifico = 'Bilobinho Amolinho Chumbolino' )
        d = Ave.objects.create( nome_cientifico = 'B. Amolinho' )
        e = Ave.objects.create( nome_cientifico = 'animaniaco' )        
        
        self.assertEqual( a.subfamilia(), '' )
        self.assertEqual( b.subfamilia(), 'Bilobinho' )
        self.assertEqual( c.subfamilia(), 'Bilobinho' )
        self.assertEqual( d.subfamilia(), 'B.' )
        self.assertEqual( e.subfamilia(), '' )


    def test_create_ave( self ):
        pato = Ave.objects.create( nome_cientifico = 'Patinho Pirilampo',
                                   nome_popular = 'Patinho',
                                   autor = '(Hugo, 1992)' )
        pato.save()
        p = Ave.objects.get( nome_cientifico__iexact = 'patinho pirilampo' )
        self.assertEqual( p.nome_cientifico, 'Patinho pirilampo' )
        self.assertEqual( p.autor, 'Hugo, 1992' )
        self.assertEqual( p.nome_popular, 'Patinho' )


class AveViewTest( TestCase ):
    def test_ave_create_unique_e_pesquisa( self ):
        resp = self.client.post( '/aves/ave/create/',
                                 data = {
                                     'nome_cientifico': 'Patinho Legalzinho',
                                     'nome_popular': 'Pato',
                                 },
                                 follow = True )
        #self.assertRedirects( resp, '/aves/ave_list/' )
        Ave.refresh_from_db()
        self.assertEqual( Ave.objects.count(), 1)        
        

        
        
        

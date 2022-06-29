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
        self.assertEqual( pick_val_in_choice( BLAPU_TEST, 'MA' ), 'Mandioca' )
        self.assertEqual( pick_val_in_choice( BLAPU_TEST, 'MC' ), 'Maçã' )
        self.assertEqual( pick_val_in_choice( BLAPU_TEST, 'OI' ), None )
        self.assertEqual( pick_val_in_choice( BLAPU_TEST, 'oi' ), None )
        self.assertEqual( pick_val_in_choice( BLAPU_TEST, '' ), None )
        self.assertEqual( pick_val_in_choice( (), '' ), None )
        self.assertEqual( pick_val_in_choice( (), 'dsafkçladsçklf' ), None )
        self.assertEqual( pick_val_in_choice( BLAPU_TEST, 'ma' ), 'Mandioca' )
        self.assertEqual( pick_val_in_choice( BLAPU_TEST, 'lH' ), 'Coelho' )
        self.assertEqual( pick_val_in_choice( BLAPU_TEST, '  lH  ' ), 'Coelho' )

    def test_choice_from_display_name( self ):
        self.assertEqual( choice_from_display_name( BLAPU_TEST, 'MA' ), None )
        self.assertEqual( choice_from_display_name( BLAPU_TEST, 'mandioca' ), 'MA' )
        self.assertEqual( choice_from_display_name( BLAPU_TEST, 'Mandioca' ), 'MA' )
        self.assertEqual( choice_from_display_name( BLAPU_TEST, '   MandiocA   ' ), 'MA' )
        self.assertEqual( choice_from_display_name( BLAPU_TEST, 'afsdflasdo' ), None )
        self.assertEqual( choice_from_display_name( BLAPU_TEST, 'maçã' ), 'MC' )        

    

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
        self.assertEqual( p.nome_cientifico, 'Patinho Pirilampo' )
        self.assertEqual( p.autor, '(Hugo, 1992)' )
        self.assertEqual( p.nome_popular, 'Patinho' )


        

        
        
class OrdemTest( TestCase ):
    def test_quantidade_aves( self ):
        b = Ordem.objects.create( nome = 'Blop' )
        b.save()
        self.assertEqual( b.quantidade_aves(), 0 )

        f = b.familia_set.create( nome = 'Flop' )
        f.save()
        g = b.familia_set.create( nome = 'Blab' )
        g.save()
        self.assertEqual( b.quantidade_aves(), 0 )

        ve = f.ave_set.create( nome_cientifico = 'Pato' )
        ve.save()
        self.assertEqual( b.quantidade_aves(), 1 )
        ve = g.ave_set.create( nome_cientifico = 'Galinha' )
        ve.save()
        self.assertEqual( b.quantidade_aves(), 2 )

        for blob in "abcdefgh":
            ve = f.ave_set.create( nome_cientifico = blob )
            ve.save()

        self.assertEqual( b.quantidade_aves(), 10 )

        for blob in "1234567890":
            ve = g.ave_set.create( nome_cientifico = blob )
            ve.save()

        self.assertEqual( b.quantidade_aves(), 20 )

class ClassifiExtraTest( TestCase ):
    def test_aves_count( self ):
        o = ClassifiExtra.objects.create( classe = 'Bilobonhos' )
        o.save()
        self.assertEqual( o.aves_count(), 0 )

        gordos = o.ordem_set.create( nome = 'Gordos' )
        gordos.save()
        bilobos = o.ordem_set.create( nome = 'Bilobos' )
        bilobos.save()

        self.assertEqual( o.aves_count(), 0 )

        for s in "0123456789":
            f = gordos.familia_set.create( nome = s )
            f.save()
            for num in range( 5 ):
                a = f.ave_set.create( nome_cientifico = s + str( num ))
                a.save()
                

        self.assertEqual( o.aves_count(), 10 * 5)

        bilob = "abcde"
        for s in bilob:
            f = bilobos.familia_set.create( nome = s )
            f.save()
            for num in range( 7 ):
                a = f.ave_set.create( nome_cientifico = s + str( num ))
                a.save()

        self.assertEqual( o.aves_count(), 10 * 5 + ( len( bilob ) * 7 ))
        
        

        
        
    
class ViewsTest( TestCase ):
    def setUp( self ):
        self.poggers = ClassifiExtra.objects.create( classe = 'Poggers',
                                                     filo = 'Inúteis',
                                                     reino = 'Cornos' )
        self.poggers.save()
        
        self.blapus = Ordem.objects.create( nome = 'Blapus',
                                            classifiextra = self.poggers)
        self.blapus.save()
        self.patoncios = Familia.objects.create( nome = 'Patôncios',
                                                 autor = 'Lolão, 2021',
                                                 ordem = self.blapus )
        
        self.patoncios.save()
        self.pato = Ave.objects.create( nome_cientifico = 'Patolino patinho',
                                        nome_popular = 'Patópolis',
                                        autor = 'Hugo, 1998',
                                        familia = self.patoncios )
        self.pato.save()        

        
    def test_ave_detail( self ):
        pato = self.pato
        
        resp = self.client.get( reverse( 'aves:ave_detail', args = [ 12321387 ]))
        self.assertEqual( resp.status_code, HTTPStatus.NOT_FOUND )


        resp = self.client.get( reverse( 'aves:ave_detail', args = [ pato.pk ]))
        self.assertEqual( resp.status_code, HTTPStatus.OK )
        self.assertContains( resp, 'Patôncios', )
        self.assertContains( resp, 'P. patinho' )
        self.assertContains( resp, '(Hugo, 1998)')
        self.assertContains( resp, 'Patópolis' )
        self.assertContains( resp, '(Lolão, 2021)' )
        self.assertContains( resp, 'Blapus' )
        self.assertContains( resp, 'Inúteis' )                


    def test_ave_edit( self ):
        resp = self.client.get( reverse( 'aves:ave_edit', args = [ 321321321 ] ))
        self.assertEqual( resp.status_code, HTTPStatus.NOT_FOUND )

        resp = self.client.get( reverse( 'aves:ave_edit', args = [ self.pato.pk ] ))
        self.assertEqual( resp.status_code, HTTPStatus.OK )

        

        resp = self.client.post( reverse( 'aves:ave_edit', args = [ self.pato.pk ] ),
                                 data = {
                                     'nome_cientifico': 'Patão Pilópilo',
                                     'info': 'Patinho incrível e supremo',
                                 },
                                 follow = True)
        self.assertEqual( resp.status_code, HTTPStatus.OK )
        self.assertContains( resp, 'supremo' )                        


    def test_classifi_edit( self ):
        resp = self.client.post( reverse( 'aves:classifi_edit', args = [ 321321321 ] ))
        self.assertEqual( resp.status_code, HTTPStatus.NOT_FOUND )

        pk = self.pato.familia.ordem.classifiextra.pk
        resp = self.client.post( reverse( 'aves:classifi_edit', args = [ pk ]),
                                 data = {
                                     'reino': 'AAAAAAAAAAAAAAA',
                                     'filo': 'Filoliloídes',
                                 },
                                 follow = True )
        self.assertEqual( resp.status_code, HTTPStatus.OK )


    def test_ordem_edit( self ):
        resp = self.client.post( reverse( 'aves:ordem_edit', args = [ 321321321 ] ))
        self.assertEqual( resp.status_code, HTTPStatus.NOT_FOUND )

        pk = self.pato.familia.ordem.pk
        resp = self.client.get( reverse( 'aves:ordem_edit', args = [ pk ] ))
        self.assertEqual( resp.status_code, HTTPStatus.OK )

        resp = self.client.post(  reverse( 'aves:ordem_edit', args = [ pk ] ),
                                  data = {
                                      'nome': 'blopu',
                                  },
                                  follow = True )
        self.assertContains( resp, 'blopu' )
        

                                
    def test_ave_create( self ):
        resp = self.client.get( reverse( 'aves:ave_create' ))
        self.assertEqual( resp.status_code, HTTPStatus.OK )
        
        resp = self.client.post( reverse( 'aves:ave_create' ),
                                 data = {
                                     'nome_cientifico': '',
                                     'nome_popular': 'Pato',
                                 },)
        self.assertEqual( resp.status_code, HTTPStatus.OK )

        resp = self.client.post( reverse( 'aves:ave_create' ),
                                 data = {
                                     'nome_cientifico': 'Corujo corujoda',
                                     'nome_popular': 'Coruja',
                                 },)        
        self.assertEqual( resp.status_code, HTTPStatus.OK )

        resp = self.client.post( reverse( 'aves:ave_create' ),
                                 data = {
                                     'nome_cientifico': 'Patolino patinho',
                                     'nome_popular': 'Erro :(',
                                 })
        self.assertContains( resp, 'já existe' )

                                 
                    
                                 


                                 
      
        #self.assertRedirects( resp, '/aves/ave_list/' )


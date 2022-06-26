"""Popula o banco de dados com as informações dos arquivos .csv gerados da plánilha."""

from aves.models import Ave, Familia, Ordem, ClassifiExtra
import csv
import os

def run():
    
    #Ave.objects.all().delete()

    ave_cri = 0
    ave_rec = 0
    ordem_cri = 0
    ordem_rec = 0
    familia_cri = 0
    familia_rec = 0    
    
    with open( 'scripts/avesPEFI.csv' ) as f:
        reader = csv.DictReader( f, delimiter = ';', quotechar = '"' )

        classifi_aves, _ = ClassifiExtra.objects.get_or_create(
            classe = 'Aves',
            filo = 'Chordata',
            reino = 'Animalia' )

        for row_count, row in enumerate( reader, 1 ):

            print( f"Linha {row_count}:" )


            # Separa nome ciêntifico
            nc_row = row[ 'Nomes científicos' ]
            nome_cientifico = nc_row.strip()
            autor = ''
            nome_comp = nome_cientifico
            if ( autor_pos := nc_row.find( '(' ) ) >= 0: # se possui o (Nome, Ano) na string de nome
                nome_cientifico = nc_row[ 0 : autor_pos ].strip()
                autor = nc_row[ autor_pos : ].replace( '(', '' ).replace( ')', '' )
                nome_comp = f"{nome_cientifico} ({autor})"


            #Cria ou ordem
            ordem_nome = row[ 'Família' ].strip().capitalize()
            ordem_ave, created = Ordem.objects.get_or_create(
                classifiextra = classifi_aves,
                nome = ordem_nome )


            print( f"\tOrdem {'criada' if created else 'recuperada'} - {ordem_ave}" )
            if created:
                ordem_cri += 1
            else:
                ordem_rec += 1

            #Cria família
            familia_nome = row[ 'Família' ].strip().capitalize()
            familia_ave, created = Familia.objects.get_or_create(
                ordem = ordem_ave,
                nome = familia_nome )
            print( f"\tFamília {'criada' if created else 'recuperada'} - {familia_ave}" )
            if created:
                familia_cri += 1
            else:
                familia_rec += 1


            #Cria ave
            ave, created = Ave.objects.get_or_create(
                familia = familia_ave,
                nome_cientifico = nome_cientifico,
                autor = autor,
                nome_popular = row[ 'Nomes populares' ].strip().capitalize(),
                frequencia_ocorrencia = row[ 'FO' ] if row[ 'FO' ].strip() != '' else None,
                abundancia_relativa = row[ 'AL' ] )
            print( f"\tAve {'criada' if created else 'recuperada'} - {ave}" )
            print( '' )

            if created:
                ave_cri += 1
            else:
                ave_rec += 1

                
        print( 'Resumo:' )
        print( f'\tAves: Criadas:\t{ave_cri}, Recuperadas:\t{ave_rec}' )
        print( f'\tFamilias: Criadas:\t{familia_cri}, Recuperadas:\t{familia_rec}' )
        print( f'\tOrdem: Criadas:\t{ordem_cri}, Recuperadas:\t{ordem_rec}' )            


            
            
            

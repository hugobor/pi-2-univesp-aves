from movies.models import Film, Genre
import csv

def run():
    with open( 'movies/pixar.csv' ) as f:
        reader = csv.reader( f )
        next( reader )

        for row in reader:
            print( row )

            genre, _ = Genre.objects.get_or_create( name = row[ -1 ])

            film, created = Film.objects.get_or_create( title = row[ 0 ],
                                                        length = row[ 1 ],
                                                        year = row[ 2 ],
                                                        genre = genre )
            if created:
                film.save()

import constants
import fresh_tomatoes
import media
from api import TheMovieDB

# Regisger an account on TheMovieDB and get a developer API
API_KEY = ''


def _convert_to_movies(the_movie_db, raw_movies):
    """
    Convert TheMovieDB movies to fresh tomatoes format
    :param the_movie_db: the movie db handler
    :param raw_movies: result from fresh tomatoes api
    :return: movies: fresh tomato movies format
    """

    movies = list()
    for movie in raw_movies:
        poster = ""
        if 'poster_path' in movie:
            poster = constants.POSTER_URL + movie['poster_path']

        success, movie_trailer_url = the_movie_db.get_movie_trailer(movie['id'])
        if not success:
            print "something went wrong with movie: {}".format(movie['id'])

        movies.append(
            media.Movie(movie['title'], poster, movie_trailer_url)
        )

    return movies


def main():
    """
        Get the popular movies from the movie db and populate it to web page.
    """
    the_movie_db = TheMovieDB(API_KEY)
    success, movies = the_movie_db.discover_movies()
    if not success:
        print "something went wrong with the api, please check"
        exit(1)

    fresh_potatoes = _convert_to_movies(the_movie_db, movies)
    fresh_tomatoes.open_movies_page(fresh_potatoes)


if __name__ == '__main__':
    main()

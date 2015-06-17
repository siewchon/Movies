import webbrowser
import datetime

class Movie():
    """ This class provides a way to store movie related information """

    VALID_LISTING = ['G', 'PG', 'PG-13', 'R']       # a constant, a class variable

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube,movie_rating,movie_type,directors,starring,movie_release_date, movie_length):
        """ The constructor that will create unique space for instance of Movie. """
        # param self is the object being created, it represents the instantiated object name
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube      # they are instance variables
        self.rating = movie_rating
        self.type = movie_type
        self.actors = starring
        self.release_date = movie_release_date.strftime("%d %B %Y")
        self.directors = directors
        self.length = movie_length

    def play_movie(self):
        """ This function will open and play the movie in a new page (tab) if possible on the web browser. """
        webbrowser.open(self.trailer_youtube_url, new=2)

    def show_trailer(self):
        """ This function will open and show the movie trailer in a web browser. """
        webbrowser.open(self.trailer_youtube_url)

    def __repr__(self):
        """ This function is created to list the set of class data members available for this Movie class """
        return "<Movie title:%s\n storyline:%s\n poster_image_url:%s\n trailer_youtube_url:%s\n rating:%s\n type:%s\n directors:%s\n actors:%s\n release_date:%s>" % (self.title, self.storyline, self.poster_image_url, self.trailer_youtube_url, self.rating, self.type, self.directors, self.actors, self.release_date)
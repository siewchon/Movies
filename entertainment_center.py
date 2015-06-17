import datetime                 # needed data object to format movie release date
import fresh_tomatoes
import media

# This file holds a list of all of my favorite movies that will be displayed on
#  the browser for quick viewing.
#  The parameter arguments needed for each movie are listed in the sequence below:
#       title of the movie
#       a short description about the movie
#       an URL link to the movie poster/image online
#       an URL link to the movie trailer online
#       movie rating
#       types of movie
#       the director(s)
#       the actors starring in the show
#       movie length

big_hero_6 = media.Movie("Big Hero 6",
                                        "The special bond that develops between plus-sized inflatable robot Baymax, and prodigy Hiro Hamada, who team up with a group of friends to form a band of high-tech heroes.",
                                        "http://ia.media-imdb.com/images/M/MV5BMjI4MTIzODU2NV5BMl5BanBnXkFtZTgwMjE0NDAwMjE@._V1_SY317_CR0,0,214,317_AL_.jpg",
                                        "www.youtube.com/watch?v=z3biFxZIJOQ",
                                        "PG",
                                        "Animation, Action, Adventure",
                                        "Don Hall, Chris Williams",
                                        "Ryan Potter, Scott Adsit, Jamie Chung",
                                        datetime.date(2014, 11, 7),
                                        "102" )

frozen = media.Movie("Frozen",
                                "The story of a fearless princess who sets off on an epic journey alongside a rugged iceman, his loyal pet reindeer, and a naive snowman to find her estranged sister, whose icy powers have inadvertently trapped the kingdom in eternal winter.",
                                "https://i.ytimg.com/vi/XfRY0ASZHuU/movieposter.jpg?v=52d8a221",
                                "https://www.youtube.com/watch?v=TbQm5doF_Uc",
                                "PG",
                                "Animation, Adventure, Comedy",
                                "Chris Buck, Jennifer Lee",
                                "Kristen Bell, Idina Menzel, Jonathan Groff",
                                datetime.date(2013, 11, 27),
                                "102" )

mulan = media.Movie("Mulan",
                                "To save her father from death in the army, a young maiden secretly goes in his place and becomes one of China's greatest heroines in the process.",
                                "http://upload.wikimedia.org/wikipedia/en/a/a3/Movie_poster_mulan.JPG",
                                "https://www.youtube.com/watch?v=wAbGAkkOgcM",
                                "G",
                                "Animation, Adventure, Family",
                                "Tony Bancroft, Barry Cook",
                                "Ming-Na Wen, Eddie Murphy, BD Wong",
                                datetime.date(1998, 6, 19),
                                "88" )

rush_hours = media.Movie("Rush Hours",
                                "Two cops who are from different worlds and can't stand each other team up to get back a kidnapped daughter.",
                                "http://upload.wikimedia.org/wikipedia/en/5/55/Rush_hour_ver2.jpg",
                                "https://youtu.be/JMiFsFQcFLE",
                                "PG-13",
                                "Action, Comedy, Crime",
                                "Brett Ratner",
                                "Jackie Chan, Chris Tucker, Ken Leung",
                                datetime.date(1998, 9, 18),
                                "98" )

pitch_perfect = media.Movie("Pitch Perfect",
                                "The plot follows a college women's a cappella group, The Barden Bellas, as they compete against another a cappella group from their college to win Nationals.",
                                "http://upload.wikimedia.org/wikipedia/en/b/b9/Pitch_Perfect_movie_poster.jpg",
                                "https://youtu.be/8dItOM6eYXY",
                                "PG-13",
                                "Comedy, Music, Romance",
                                "Jason Moore",
                                "Anna Kendrick, Brittany Snow, Rebel Wilson",
                                datetime.date(2012, 10, 5),
                                "112" )

avatar = media.Movie("Avatar",
                                    "A marine on an alien planet",
                                    "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                                    "https://youtu.be/5PSNL1qE6VY",
                                    "PG-13",
                                    "Action, Adventure, Fantasy",
                                    "James Cameron",
                                    "Sam Worthington, Zoe Saldana, Sigourney Weaver",
                                    datetime.date(2009, 12, 18),
                                    "162" )
#avatar.show_trailer()

# a list of movies titles that are going to be displayed on the web browser
movies = [big_hero_6, frozen, mulan, rush_hours, pitch_perfect, avatar]
fresh_tomatoes.open_movies_page(movies)    # this opens a browser with list of movies display on the page

#print media.Movie.VALID_LISTING
#print (media.Movie.__module__)   # predefined class attributes - ret. media
#print (media.Movie.play_movie.__doc__)             # ret. the doc info about this class
#print (media.Movie.__name__)   # predefined class attributes - ret. class name: Movie
#print (media.Movie.__bases__)   # predefined class attributes - ret. The classes from which this class inherits., but not for this one
#print (media.Movie.__repr__)       # AttributeError: class Movie has no attribute '__repr__'
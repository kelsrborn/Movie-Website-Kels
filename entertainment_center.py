import fresh_tomatoes
import media

sweet_home_alabama = media.Movie("Sweet Home Alabama",
                                  "a new york fashion designer finds herself back home in her small town dealing with troubles from the past",
                                  "https://upload.wikimedia.org/wikipedia/en/thumb/f/fc/Sweet_Home_Alabama_film.jpg/220px-Sweet_Home_Alabama_film.jpg",
                                  "https://www.youtube.com/watch?v=BM89EgWx_Gs")


oh_brother_where_art_thou = media.Movie("Oh Brother Where Art Thou",
                                        "three escaped covicts search for hidden treasure while being persued by a lawman",
                                        "https://images-na.ssl-images-amazon.com/images/I/5107M4P37AL.jpg",
                                        "https://www.youtube.com/watch?v=eW9Xo2HtlJI")

                                        
the_blind_side = media.Movie("The Blind Side",
                             "The true story of baltimore ravens offensive left tackle Michael Oher",
                             "http://www.gstatic.com/tv/thumb/movieposters/3538632/p3538632_p_v8_aq.jpg",
                             "https://www.youtube.com/watch?v=gvqj_Tk_kuM")

the_devil_wears_prada = media.Movie("The Devil Wears Prada",
                                    "A simple and naive graduate in journalism is hired to work as an assistant to a power magazine editor",
                                    "https://upload.wikimedia.org/wikipedia/en/e/e7/The_Devil_Wears_Prada_main_onesheet.jpg",
                                    "https://www.youtube.com/watch?v=XTDSwAxlNhc")

bride_wars = media.Movie("Bride Wars",
                         "two best friends become rivals when they schedule their weddings on the same day",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BMTUyNTg2OTUwN15BMl5BanBnXkFtZTgwNzEzMzg5MTI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                         "https://www.youtube.com/watch?v=n843e1Gilbk")

up = media.Movie("Up",
                 "a 78 year old balloon salesman is about to fulfill his lifelong dream",
                 "https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg",
                 "https://www.youtube.com/watch?v=pkqzFUhGPJg")

movies = [sweet_home_alabama, oh_brother_where_art_thou, the_blind_side, the_devil_wears_prada, bride_wars, up]
fresh_tomatoes.open_movies_page(movies)


import webapp2
from random import shuffle
import jinja2
import os
from random import randint




the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    


    
class Welcome(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/welcome.html')
        self.response.write(about_template.render())
        
    
        
   
class Comedy(webapp2.RequestHandler):
    def get(self):
        spot = randint(0,4)
        about_template = the_jinja_env.get_template('templates/comedy.html')
        comedy_movies = ['https://www.youtube.com/embed/cd-go0oBF4Y','https://www.youtube.com/embed/CXqxP-bUC7I',
        'https://www.youtube.com/embed/l13yPhimE3o','https://www.youtube.com/embed/D6gABQFR94U','https://www.youtube.com/embed/MNpoTxeydiY']
        comedy_movies_title = ['The Big Lebowski','Meet the Parents','Dumb and Dumber','Ferris Buellers Day Off','SuperBad']
        comedy_movies_director = ['Ethan and Joel Cohen', 'Jay Roach', 'Peter Farrelly', 'John Hughes', 'Greg Mottola']
        comedy_movies_descriptions = ['Jeff "The Dude" Leboswki is mistaken for Jeffrey Lebowski, who is The Big Lebowski. Which explains why he is roughed up and has his precious rug peed on. In search of recompense, The Dude tracks down his namesake, who offers him a job. His wife has been kidnapped and he needs a reliable bagman. Aided and hindered by his pals Walter Sobchak, a Vietnam vet, and Donny, master of stupidity.',
        'A young mans first visit to his girlfriends parents house turns out to be more nightmarish than he could ever have imagined. Hoping to use the weekend as a chance to propose to his girlfriend, he only succeeds in incurring the wrath of his prospective father-in-law and almost destroys their home in the process.',
        'Imbecilic best friends Lloyd Christmas (Jim Carrey) and Harry Dunne (Jeff Daniels) stumble across a suitcase full of money left behind in Harrys car by Mary Swanson (Lauren Holly), who was on her way to the airport. The pair decide to go to Aspen, Colo., to return the money, unaware that it is connected to a kidnapping. As Harry and Lloyd -- who has fallen in love with Mary -- are pursued across the country by hired killers and police, they find both their friendship and their brains tested.',
        'Ferris Bueller (Matthew Broderick) has an uncanny skill at cutting classes and getting away with it. Intending to make one last duck-out before graduation, Ferris calls in sick, "borrows" a Ferrari, and embarks on a one-day journey through the streets of Chicago. On Ferris trail is high school principal Rooney (Jeffrey Jones), determined to catch him in the act.'
        'Two inseparable best friends navigate the last weeks of high school and are invited to a gigantic house party. Together with their nerdy friend, they spend a long day trying to score enough alcohol to supply the party and inebriate two girls in order to kick-start their sex lives before they go off to college. Their quest is complicated after one of them falls in with two inept cops who are determined to show him a good time.']
        movie_pick = comedy_movies[spot]
        movie_title_pick = comedy_movies_title[spot]
        movie_director = comedy_movies_director[spot]
        movie_description = comedy_movies_descriptions[spot]
        comedy_dict = {
            'movie_trailer': movie_pick,
            'movie_title': movie_title_pick,
            'movie_director': movie_director,
            'movie_description': movie_description
        }
        self.response.write(about_template.render(comedy_dict))
    
class Drama(webapp2.RequestHandler):
    def get(self):
        spot = randint(0,4)
        about_template = the_jinja_env.get_template('templates/drama.html')
        drama_movies = ['https://www.youtube.com/embed/lB95KLmpLR4','https://www.youtube.com/embed/5gcyB72nFmc',
        'https://www.youtube.com/embed/89Kq8SDyvfg','https://www.youtube.com/embed/6hB3S9bIaco','https://www.youtube.com/embed/M5FpB6qDGAE']
        drama_movies_title = ['The Social Network','The Imitation Game','The Pursuit of Happyness','The Shawshank Redemption','Schindlers List']
        drama_movies_director = ['David Fincher', 'Morten Tyldum', 'Gabriele Muccino', 'Frank Darabont', 'Steven Spielberg']
        drama_movies_description = ['In 2003, Harvard undergrad and computer genius Mark Zuckerberg (Jesse Eisenberg) begins work on a new concept that eventually turns into the global social network known as Facebook. Six years later, he is one of the youngest billionaires ever, but Zuckerberg finds that his unprecedented success leads to both personal and legal complications when he ends up on the receiving end of two lawsuits, one involving his former friend (Andrew Garfield). Based on the book "The Accidental Billionaires."',
        'In 1939, newly created British intelligence agency MI6 recruits Cambridge mathematics alumnus Alan Turing (Benedict Cumberbatch) to crack Nazi codes, including Enigma -- which cryptanalysts had thought unbreakable. Turings team, including Joan Clarke (Keira Knightley), analyze Enigma messages while he builds a machine to decipher them. Turing and team finally succeed and become heroes, but in 1952, the quiet genius encounters disgrace when authorities reveal he is gay and send him to prison.',
        'Life is a struggle for single father Chris Gardner (Will Smith). Evicted from their apartment, he and his young son (Jaden Christopher Syre Smith) find themselves alone with no place to go. Even though Chris eventually lands a job as an intern at a prestigious brokerage firm, the position pays no money. The pair must live in shelters and endure many hardships, but Chris refuses to give in to despair as he struggles to create a better life for himself and his son.',
        'Andy Dufresne (Tim Robbins) is sentenced to two consecutive life terms in prison for the murders of his wife and her lover and is sentenced to a tough prison. However, only Andy knows he did not commit the crimes. While there, he forms a friendship with Red (Morgan Freeman), experiences brutality of prison life, adapts, helps the warden, etc., all in 19 years.',
        'Businessman Oskar Schindler (Liam Neeson) arrives in Krakow in 1939, ready to make his fortune from World War II, which has just started. After joining the Nazi party primarily for political expediency, he staffs his factory with Jewish workers for similarly pragmatic reasons. When the SS begins exterminating Jews in the Krakow ghetto, Schindler arranges to have his workers protected to keep his factory in operation, but soon realizes that in so doing, he is also saving innocent lives.']
        movie_pick = drama_movies[spot]
        movie_title_pick = drama_movies_title[spot]
        movie_director = drama_movies_director[spot]
        movie_description = drama_movies_description[spot]
        drama_dict = {
            'movie_trailer': movie_pick,
            'movie_title': movie_title_pick,
            'movie_director': movie_director,
            'movie_description': movie_description
        }
        self.response.write(about_template.render(drama_dict))

class Horror(webapp2.RequestHandler):
    def get(self):
        spot = randint(0,4)
        about_template = the_jinja_env.get_template('templates/horror.html')
        horror_movies = ['https://www.youtube.com/embed/k10ETZ41q5o','https://www.youtube.com/embed/k5WQZzDRVtw',
        'https://www.youtube.com/embed/F_UxLEqd074','https://www.youtube.com/embed/a_Hw4bAUj8A','https://www.youtube.com/embed/lQKs169Sl0I']
        horror_movies_title = ['The Conjuring','The Babadook','Paranormal Activity','The Blair Witch Project','The Silence of the Lambs']
        horror_movies_director = ['James Wan', 'Jennifer Kent', 'Oren Peli', 'Eduardo Sanchez', 'Jonathan Demme']
        horror_movies_description = ['In 1970, paranormal investigators and demonologists Lorraine (Vera Farmiga) and Ed (Patrick Wilson) Warren are summoned to the home of Carolyn (Lili Taylor) and Roger (Ron Livingston) Perron. The Perrons and their five daughters have recently moved into a secluded farmhouse, where a supernatural presence has made itself known. Though the manifestations are relatively benign at first, events soon escalate in horrifying fashion, especially after the Warrens discover the houses macabre history.',
        'A single mother, plagued by the violent death of her husband, battles with her sons fear of a monster lurking in the house, but soon discovers a sinister presence all around her.',
        'After moving into a suburban home, a couple becomes increasingly disturbed by a nightly demonic presence.',
        'Found video footage tells the tale of three film students (Heather Donahue, Joshua Leonard, Michael C. Williams) who have traveled to a small town to collect documentary footage about the Blair Witch, a legendary local murderer. Over the course of several days, the students interview townspeople and gather clues to support the tales veracity. But the project takes a frightening turn when the students lose their way in the woods and begin hearing horrific noises.',
        'Jodie Foster stars as Clarice Starling, a top student at the FBIs training academy. Jack Crawford (Scott Glenn) wants Clarice to interview Dr. Hannibal Lecter (Anthony Hopkins), a brilliant psychiatrist who is also a violent psychopath, serving life behind bars for various acts of murder and cannibalism. Crawford believes that Lecter may have insight into a case and that Starling, as an attractive young woman, may be just the bait to draw him out.']
        movie_pick = horror_movies[spot]
        movie_title_pick = horror_movies_title[spot]
        movie_director = horror_movies_director[spot]
        movie_description = horror_movies_description[spot]
        horror_dict = {
            'movie_trailer': movie_pick,
            'movie_title': movie_title_pick,
            'movie_director': movie_director,
            'movie_description': movie_description
        }
        self.response.write(about_template.render(horror_dict))

class Action(webapp2.RequestHandler):
    def get(self):
        spot = randint(0,4)
        about_template = the_jinja_env.get_template('templates/action.html')
        action_movies = ['https://www.youtube.com/embed/bvaftiAu7mw','https://www.youtube.com/embed/gKTVQPOH8ZA',
        'https://www.youtube.com/embed/pbA-tBrHNfI','https://www.youtube.com/embed/c4Jo8QoOTQ4','https://www.youtube.com/embed/0ZOcoxjeUYo']
        action_movies_title = ['John Wick','Training Day','Taken','The Terminator','Raiders of the Lost Ark']
        action_movies_director = ['Chad Stahelski', 'Antoine Fuqua', 'Pierre Morel', 'James Cameron', 'Steven Spielberg']
        movie_pick = action_movies[spot]
        movie_title_pick = action_movies_title[spot]
        movie_director = action_movies_director[spot]
        action_dict = {
            'movie_trailer': movie_pick,
            'movie_title': movie_title_pick,
            'movie_director': movie_director
        }
        self.response.write(about_template.render(action_dict))
    
class Mystery(webapp2.RequestHandler):
    def get(self):
        spot = randint(0,4)
        about_template = the_jinja_env.get_template('templates/mystery.html')
        mystery_movies = ['https://www.youtube.com/embed/5iaYLCiq5RM','https://www.youtube.com/embed/66TuSJo4dZM',
        'https://www.youtube.com/embed/0vS0E9bBSL0','https://www.youtube.com/embed/bEvnwKFUnI0','https://www.youtube.com/embed/J4YV2_TcCoE']
        mystery_movies_title = ['Shutter Island','Inception','Memento','Zodiac','Se7en']
        mystery_movies_director = ['Martin Scorsese', 'Christopher Nolan', 'Christopher Nolan', 'David Fincher', 'David Fincher']
        movie_pick = mystery_movies[spot]
        movie_title_pick = mystery_movies_title[spot]
        movie_director = mystery_movies_director[spot]
        mystery_dict = {
            'movie_trailer': movie_pick,
            'movie_title': movie_title_pick,
            'movie_director': movie_director
            
           # 'movie-description': 
        }
        self.response.write(about_template.render(mystery_dict))
        
        
app = webapp2.WSGIApplication([
    ('/', Welcome),
    ('/comedy', Comedy),
    ('/drama', Drama),
    ('/horror', Horror),
    ('/action', Action),
    ('/mystery', Mystery)
], debug=True)
'''
Program: sentenceGenerator.py
Chapter 5 Case Study (page 129 - 132)
9/14/2026

Application that generates and displays sentences using simple grammar. Each small process will be it's own function. The user will input the number of sentences to generate. Words are chosen at random.
'''

import random

# Global variables containing the tuple lists with different parts of speech that ALL our functions can use.
articles = ('A', 'AN', 'THE')

nouns = ('DOG', 'CAT', 'MAN', 'WOMAN', 'CHILD', 'TEACHER', 'STUDENT', 'DOCTOR', 'ARTIST', 'MUSICIAN', 'SCIENTIST', 'FARMER', 'CHEF', 'PILOT', 'SAILOR', 'BIRD', 'RABBIT', 'HORSE', 'TURTLE', 'LION', 'FOX', 'BEAR', 'MOUSE', 'DRAGON', 'ROBOT', 'FRIEND', 'NEIGHBOR', 'TRAVELER', 'EXPLORER', 'KING', 'QUEEN', 'GARDEN', 'FOREST', 'RIVER', 'MOUNTAIN', 'VILLAGE', 'CITY', 'CASTLE', 'SCHOOL', 'LIBRARY', 'COMPUTER', 'BOOK', 'BICYCLE', 'CAR', 'ACTOR', 'AUTHOR', 'BAKER', 'CAPTAIN', 'DANCER', 'DETECTIVE', 'ENGINEER', 'FIREFIGHTER', 'GARDENER', 'HERO', 'INVENTOR', 'JUDGE', 'KNIGHT', 'LEADER', 'MAGICIAN', 'NURSE', 'OFFICER', 'POET', 'REPORTER', 'SINGER', 'SOLDIER', 'WIZARD', 'WOLF', 'EAGLE', 'DOLPHIN', 'ELEPHANT', 'GIRAFFE', 'MONKEY', 'PENGUIN', 'SHARK', 'TIGER', 'WHALE', 'BUTTERFLY', 'OWL', 'SNAKE', 'OCEAN', 'ISLAND', 'DESERT', 'VALLEY', 'WATERFALL', 'MEADOW', 'BEACH', 'PLANET', 'STAR', 'MOON', 'CLOUD', 'STORM', 'BRIDGE', 'TOWER', 'TRAIN', 'AIRPLANE', 'BOAT', 'CAMERA', 'CLOCK', 'GUITAR', 'TELESCOPE', 'TREASURE', 'ACCOUNTANT', 'ARCHITECT', 'ASTRONAUT', 'ATHLETE', 'BARBER', 'BIOLOGIST', 'BLACKSMITH', 'BUILDER', 'CARPENTER', 'CASHIER',
'COACH', 'COMMANDER', 'COURIER', 'COWBOY', 'DIRECTOR', 'DRIVER', 'EDITOR','ELECTRICIAN', 'GUARD', 'HISTORIAN', 'JOURNALIST', 'LIBRARIAN', 'MAYOR','MECHANIC', 'MERCHANT', 'PAINTER', 'PHOTOGRAPHER', 'PLUMBER', 'PROFESSOR','PROGRAMMER', 'RANGER', 'SCULPTOR', 'SHERIFF', 'TAILOR', 'VETERINARIAN', 'WAITER','WRITER', 'ALLIGATOR', 'ANT', 'BEE', 'CAMEL', 'CHEETAH', 'CHICKEN', 'CROCODILE','DEER', 'DONKEY', 'DUCK', 'FALCON', 'FROG', 'GOAT', 'GORILLA', 'HAMSTER', 'HAWK','KANGAROO', 'KOALA', 'LEOPARD', 'LIZARD', 'OCTOPUS', 'OTTER', 'PANDA', 'PARROT','PEACOCK', 'RACCOON', 'SEAL', 'SHEEP', 'SPIDER', 'SQUIRREL', 'SWAN', 'ZEBRA','CANYON', 'CAVE', 'CLIFF', 'FIELD', 'GLACIER', 'HARBOR', 'HILL', 'JUNGLE', 'LAKE','MARSH', 'POND', 'PRAIRIE', 'RAINFOREST', 'STREAM', 'SWAMP', 'TRAIL', 'VOLCANO','CABIN', 'FACTORY', 'FARM', 'HOSPITAL', 'HOTEL', 'MARKET', 'MUSEUM', 'PALACE','PARK', 'RESTAURANT', 'STADIUM', 'STATION', 'THEATER',)

verbs = ('RUNS', 'JUMPS', 'TALKS', 'SLEEPS', 'EATS', 'WALKS', 'LAUGHS', 'SMILES', 'READS','WRITES', 'SINGS', 'DANCES', 'SWIMS', 'CLIMBS', 'FLIES', 'DRIVES', 'COOKS','PAINTS', 'DRAWS', 'LISTENS', 'WATCHES', 'LEARNS', 'TEACHES', 'EXPLORES','TRAVELS', 'BUILDS', 'CREATES', 'DISCOVERS', 'SEARCHES', 'PLAYS', 'WORKS', 'RESTS','DREAMS', 'THINKS', 'SPEAKS', 'WAITS', 'WANDERS', 'ARRIVES', 'RETURNS','CELEBRATES', 'WHISPERS', 'SHOUTS', 'HELPS', 'FOLLOWS', 'ACTS', 'ADMIRES','ANSWERS', 'APPEARS', 'ASKS', 'BAKES', 'BALANCES', 'BEGINS', 'BOWS', 'CARRIES','CATCHES', 'CHANGES', 'CHOOSES', 'COLLECTS', 'CROSSES', 'DECIDES', 'DELIVERS','DIGS', 'DIVES', 'ESCAPES', 'FLOATS', 'GATHERS', 'GLIDES', 'GROWS', 'GUIDES','HIDES', 'HIKES', 'HURRIES', 'IMAGINES', 'INVENTS', 'JOINS', 'KNOCKS', 'LANDS','LEADS', 'LOOKS', 'MARCHES', 'NOTICES', 'OPENS', 'PACKS', 'REACHES', 'RIDES','ROLLS', 'SAILS', 'SHINES', 'SKIPS', 'SOLVES', 'SPINS', 'STANDS', 'STARTS','STOPS', 'STUDIES', 'SURPRISES', 'THROWS', 'VISITS', 'WAVES', 'WINS', 'ACCEPTS','ADDS', 'AGREES', 'ANNOUNCES', 'APPLAUDS', 'APPROACHES', 'ARGUES', 'AWAKENS','BLINKS', 'BORROWS', 'BOUNCES', 'BREAKS', 'BREATHES', 'BRINGS', 'BRUSHES', 'CALLS','CARES', 'CARVES', 'CHASES', 'CHEERS', 'CLEANS', 'CLOSES', 'COMES', 'COMPARES','COMPLETES', 'COUNTS', 'CRAWLS', 'CRIES', 'CUTS', 'DECORATES', 'DESCRIBES','DRINKS', 'DROPS', 'ENTERS', 'EXAMINES', 'EXPLAINS', 'FALLS', 'FEEDS', 'FEELS','FIGHTS', 'FINDS', 'FINISHES', 'FIXES', 'FORGETS', 'FORGIVES', 'FREEZES', 'GIVES','GRABS', 'GREETS', 'GRINS', 'HEARS', 'HOPS', 'HUGS', 'HUNTS', 'INVITES', 'KICKS','KNEELS', 'KNOWS', 'LIFTS', 'LOVES', 'MAKES', 'MEASURES', 'MEETS', 'MIXES','MOVES', 'NEEDS', 'NODS', 'OBSERVES', 'OFFERS', 'ORDERS', 'PASSES', 'PICKS','PLANTS', 'POINTS', 'PRACTICES', 'PULLS', 'PUSHES', 'REMEMBERS', 'REPAIRS','REPEATS', 'REPLIES', 'RESCUES', 'RISES', 'ROARS', 'SAVES', 'SEES', 'SELLS','SENDS', 'SHAKES', 'SHARES', 'SHOOTS', 'SHOWS', 'SHRUGS', 'SITS', 'SLIDES','SMELLS', 'SNEEZES', 'SPELLS', 'SPLASHES', 'STEPS',)

prepositions = ('ABOVE', 'ACROSS', 'AGAINST', 'ALONG', 'AMONG', 'AROUND', 'AT', 'BEFORE', 'BEHIND','BELOW', 'BENEATH', 'BESIDE', 'BETWEEN', 'BEYOND', 'BY', 'DURING', 'FOR', 'FROM','IN', 'INSIDE', 'INTO', 'NEAR', 'OF', 'OFF', 'ON', 'ONTO', 'OUTSIDE', 'OVER','PAST', 'THROUGH', 'THROUGHOUT', 'TO', 'TOWARD', 'UNDER', 'UNDERNEATH', 'UNTIL','UP', 'UPON', 'WITH', 'WITHIN', 'WITHOUT', 'ABOUT', 'AFTER', 'ALONGSIDE', 'AMID','AMIDST', 'AS', 'EXCEPT', 'LIKE', 'OPPOSITE', 'PER', 'PLUS', 'REGARDING', 'ROUND','SINCE', 'THAN', 'VIA', 'ACCORDING TO', 'AHEAD OF', 'APART FROM', 'AS FOR','ASIDE FROM', 'BECAUSE OF', 'CLOSE TO', 'DUE TO', 'EXCEPT FOR', 'FAR FROM','IN FRONT OF', 'IN PLACE OF', 'IN SPITE OF', 'INSTEAD OF', 'NEXT TO','ON ACCOUNT OF', 'ON BEHALF OF', 'ON TOP OF', 'OUT OF', 'PRIOR TO', 'THANKS TO','UP TO', 'ABREAST OF', 'ABSENT FROM', 'ACROSS FROM', 'ADJACENT TO', 'ALONG WITH','AMONGST', 'APART FROM', 'AS OF', 'AS PER', 'AS REGARDS', 'AWAY FROM', 'BACK OF','BARRING', 'BY MEANS OF', 'BY WAY OF', 'CIRCA', 'CONCERNING', 'CONSIDERING','CONTRARY TO', 'COUNTING', 'DEPENDING ON', 'DESPITE', 'DOWN', 'EXCEPTING','EXCLUDING', 'FOLLOWING', 'FOR THE SAKE OF', 'FOR WANT OF', 'FORTH FROM','FORWARD OF', 'IN ACCORDANCE WITH', 'IN ADDITION TO', 'IN CASE OF','IN COMPARISON WITH', 'IN CONNECTION WITH', 'IN CONTRAST TO', 'IN EXCHANGE FOR','IN FAVOR OF', 'IN LIEU OF', 'IN LIGHT OF', 'IN LINE WITH', 'IN RELATION TO','IN RESPONSE TO', 'IN SEARCH OF', 'IN TERMS OF', 'IN THE MIDST OF', 'IN VIEW OF','INCLUDING', 'INCLUSIVE OF', 'IRRESPECTIVE OF', 'LEFT OF', 'LESS', 'MINUS','NEAREST', 'NOTWITHSTANDING', 'ON', 'ON THE EDGE OF', 'ON THE FAR SIDE OF','ON THE NEAR SIDE OF', 'ON THE OTHER SIDE OF', 'ONTO', 'OPPOSITE TO', 'OUTSIDE OF','OWING TO', 'PACE', 'PENDING', 'PERTAINING TO', 'PRO', 'PURSUANT TO', 'RE','REFERENCE', 'RELATIVE TO', 'REGARDLESS OF', 'RIGHT OF', 'SAVE', 'SAVE FOR','SHORT OF', 'SUBSEQUENT TO', 'TOGETHER WITH', 'TOUCHING', 'UNDER COVER OF','UNDERNEATH', 'UNLIKE', 'UP AGAINST', 'UPON', 'VERSUS', 'VIS-A-VIS','WITH A VIEW TO', 'WITH REGARD TO', 'WITH RESPECT TO', 'WITHIN REACH OF','WITHOUT REGARD TO', 'ABOARD', 'ASTRIDE', 'ATHWART', 'BETWIXT', 'BUT','EXCEPT FOR', 'IN BETWEEN', 'NEAR TO', 'OFF OF', 'OVER AGAINST', 'PAST','ROUND ABOUT', 'THROUGHOUT', 'TILL', 'TIMES', 'UPSIDE', 'WANTING', 'BY VIRTUE OF','BY REASON OF', 'FOR FEAR OF', 'IN BACK OF', 'IN SUPPORT OF', 'ON PAIN OF','PREPARATORY TO', 'PREVIOUS TO', 'SANS', 'SUBJECT TO', 'WORTHY OF', 'AS FAR AS',)

# Definition of a sentence() function
def sentence():
    '''Builds and returns a sentence.'''
    return nounPhrase() + " " + verbPhrase()

# Definition of a nounPhrase() function
def nounPhrase():
    '''Builds and returns a noun phrase.'''
    return random.choice(articles) + " " + random.choice(nouns)

# Definition of a verbPhrase() function
def verbPhrase():
    '''Builds and returns a verb phrase.'''
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()

# Definition of a prepositionalPhrase() function
def prepositionalPhrase():
    '''Builds and returns a prepositional phrase.'''
    return random.choice(prepositions) + " " + nounPhrase()

# Definition of a main() function for program entry
def main():
    '''Prompts the user for the number of sentences to generate'''
    number = int(input("Please enter the number of sentences you'd like to see >> "))
    for count in range(number):
        print(sentence())
    # Loop is done, but we're still in main()
    input("\nSentences completed. Press ENTER to quit")

# Global call to the main() function for program execution
if __name__ == "__main__":
    main()
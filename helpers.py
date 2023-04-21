import random

descriptors =  ['agony', 'demented', 'scrimblo', 'jimbo', 'jimblo', 'dirt', 'tragedy', 'dirtbag', 'little', 'shrivelled', 'shrivelled little', 'sick', 'stupid little shrivelled little']

nouns = ['head', 'skippy', 'jokic', 'jamaldo', 'casino', 'flicky', 'G.O.A.T', 'clown', 'pepega', 'pepe', 'dumbass', 'fuck', 'agonyhead', 'scrimblo', 'phony', 'bastard', 'rat bastard', 'sick fuck', ]

phrases = ['Watch your mouth', "It's over", "Not a chance", "Shoulda had a better angle", "Watch your tongue", "Perish" ]

# write a function that creates a random insult

def random_insult():
    descriptor = random.choice(descriptors)
    noun = random.choice(nouns)
    phrase = random.choice(phrases)
    return (f'{phrase}, {descriptor} {noun}')

def desc_noun():
    descriptor = random.choice(descriptors)
    noun = random.choice(nouns)
    return (f'{descriptor} {noun}')
 
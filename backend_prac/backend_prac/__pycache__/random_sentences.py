
#5 Generate random sentences.
from random import choice

Verbs = ['goes', 'takes', 'gets', 'opens', 'sees', 'lifts',
         'tries', 'smells', 'sets up', 'leaves']
Nouns = ['dog', 'cat', 'house', 'toy', 'hair', 'water',
         'door', 'sky', 'sun', 'box']
Adjectives = ['old', 'new', 'dirty', 'shiny', 'red', 'cold',
              'fake', 'happy', 'funny', 'heavy']
print('The', choice(Adjectives), choice(Nouns), choice(Verbs), 'the', choice(Nouns)+'.')

print()

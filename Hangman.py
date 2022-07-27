import random

hangMan0 = '''
 ___
|   o
|  /|\ 

Deid!

'''
hangMan1 = '''
 ___
|   o
|   | 

1 Guess Left!

'''
hangMan2 = '''
 ___
|   o
|    

2 Guesses Left!

'''
hangMan3 = '''
 ___
|   
|    

3 Guesses Left!

'''
hangMan4 = '''

|   
|     

4 Guesses Left!

'''
hangMan5 = '''
 
   
|    

5 Guesses left!

'''

selectWord = ['dog','cat','egg']

selection = random.choice(selectWord)

print(selection)

letters = list(selection)

letter1 = letters[0]
letter2 = letters[1]
letter3 = letters[2]

g1 = '_'
g2 = '_'
g3 = '_'

guesses = g1 + g2 + g3

hangMan = 6

def turn():

  global letters
  global letter1
  global letter2
  global letter3
  global g1
  global g2
  global g3
  global guesses

  guesses = g1 + letter2 + g3
  
  print(guesses)


while len(letters) > 0:
  guess = input("Guess a letter?")
  if guess == letter1:
    print('yes')
    letters.remove(guess)
    turn()
  elif guess == letter2:
    print('yes')
    letters.remove(guess)
    turn()
  elif guess == letter3:
    print('yes')
    letters.remove(guess)
    turn()   
  else:
    hangMan -= 1
    print('Wrong')
    if hangMan == 5:
      print(hangMan5)
    if hangMan == 4:
      print(hangMan4)
    if hangMan == 3:
      print(hangMan3)
    if hangMan == 2:
      print(hangMan2)
    if hangMan == 1:
      print(hangMan1)
    if hangMan == 0:
      print(hangMan0)
      print('You Lose!')
      break
    
if len(letters) < 1:
  print('You win!')

print('end')
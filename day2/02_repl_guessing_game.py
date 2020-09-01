# lets make a guessing game
# set a value
# take in some input from a player
# check it against a value
# if they are the same print player wins
# if they are different print guess again
# and loop


# what is a REPL?
# loop that reads, eval and prints until user ends the program
# how can we make this game replayable?
import random

value = random.randrange(1, 10)
guess = 0
while value != guess:
    guess = input('Guess my number:')
    guess = int(guess)
    if guess == value:
        print('You win')
    else:
        print('Guess again')

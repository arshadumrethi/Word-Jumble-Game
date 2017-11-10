from itertools import permutations
import getpass
import random

#Game begins, player1 enters a word, getpass is used to hide the input in terminal.
print 'Player 1, Enter the word to be jumbled'
word = getpass.getpass("Word: ")

#The word is split into a list so that it may be iterated over.
word_ = list(word)

#All permutations of the characters in the word are stored in perms as a list.
perms = [''.join(p) for p in permutations(word_)]

#A random permutation is chosen from the list of words using index 1 to avoid the original word.
var = perms[random.randint(1,len(perms))]

#Player 2 is given the jumbled word and asked to enter an answer.
print 'Player 2, Try to unjumble this word : %s' % var
print 'Enter your answer'
guess = raw_input()

#Conditional statements are used to give player 2 three chances at guessing the word.
if guess == word:
    print "Wow you got it on your first try!"
elif guess != word:
    print "You guessed wrong Try again, Enter your 2nd attempt: "
    guess = raw_input()
    if guess == word:
        print "Great, you got it in the 2nd try!"
    elif guess != word:
        print "You guessed wrong, Try again, This is your last chance: "
        guess = raw_input()
        if guess == word:
            print "Finally! Your are correct"
        else:
            print "Oops! Good effort but unfortunately you lose the game."

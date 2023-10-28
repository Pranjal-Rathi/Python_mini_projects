# Hangman Game
import random
from collections import Counter

someWords = '''apple, cherry, mango, ash, loobdhi, mos, pranjuu, jungkoo, sumyaa, sumii, summii, peaches, misal,
 hehehe'''
someWords = someWords.split(", ")
word = random.choice(someWords)
length = len(word)
# print(word)
print("~~~Welcome to the Hangman Game~~~")
print('Guess a word(Name/Fruit)')
guess_count = length + 2
temp = ['-' for i in range(length)]
print(' '.join(temp))

while guess_count > 0:
    guess = input('Enter your guess: ')
    if len(guess)==length:
        for i in range(length):
            if guess.lower()[i] == word[i]:
                temp[i] = guess.lower()[i]
        print(' '.join(temp))
        guess_count -= 1
        if (''.join(temp)) == word:
            print("Congratulations...You won the game.")
            break
    else:
        print("Enter a valid guess")
if (''.join(temp)) != word:
    print("Oops...Better luck next time!!")
    print("The word was: " + word)
# Hangman Game Project by Khadeer Pathan, IIIT-H

from words import words
import random

def get_valid_words(words):
    word = random.choice(words)     # picks a random word from words list
    for i in word:
        if i.isalpha() == False:    # every value in the picked up word should be an aplhabet or else pick a new word
            word = random.choice(words)
    return word


word = get_valid_words(words)
# print(word)

import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while '_' in words or " " in words:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        # letters used
        # " ".join(["a", "b", "c"]) --> "a b c"
        print("You have", lives, " lives left. You used these letters:", ", ".join(used_letters))

        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word:", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
                print("This letter is not in the word.")

        elif user_letter in used_letters:
            print("You have already used that letter. Please try again. ")

        else:
            print("You didn't type a valid character.")

    if lives == 0:
        print("You lost the game, No live is left :( ")
    else:
        print(f"you guessed the word {word} correctly :) ")
        
hangman()


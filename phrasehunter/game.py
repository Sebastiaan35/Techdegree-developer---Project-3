#!/usr/bin/env python3
"""The game module"""
import random
from phrasehunter.phrase import Phrase
from phrasehunter.phrase_list import string_list

class Game:
    """The game class"""               
    def __init__(self):
        self.Guess = ''
        self.guesses = []
        self.missed = 0
        self.active_phrase = None
        #Credits for the beautiful list comprehension below go to: Jennifer Nordell
        self.phrases = [Phrase(phrase_string) for phrase_string in string_list]

    def start(self):
        """Method responsible for running a single game"""
        self.welcome()
        #Initialise the game phrase:
        self.start_game()
        print(self.active_phrase.display(self.guesses))
        while not self.game_over():
            self.Guess = self.get_guess()
            if not self.active_phrase.check_letter(self.Guess):
                self.missed += 1
                print(f'\nI\'m sorry. There is no \'{self.Guess}\' in this phrase...\n\n'
                f'You have {5 - self.missed} guess(es) remaining.')
            else:
                print(f'\nVery good! There is a(n) \'{self.Guess}\' in this phrase indeed.\n')
            print(self.active_phrase.display(self.guesses))

    def welcome(self):
        """Welcome message"""
        print("\nWelcome to Sebastiaan's Phrase Hunters game :)")

    def start_game(self):
        """Assign a random phrase"""
        self.active_phrase = self.get_random_phrase()

    def get_random_phrase(self):
        """Retrieve a random phrase"""
        return random.choice(self.phrases)

    def get_guess(self):
        """Get valid user input"""
        UserInputOK = False
        while not UserInputOK:
            Inputy = str(input("Please, guess a letter: ")).lower()
            if len(Inputy) == 1 and Inputy.isalpha() and Inputy not in self.guesses:
                UserInputOK = True
            elif len(Inputy) == 0:
                print("The input cannot be empty!")
            elif len(Inputy) != 1:
                print("Please, type only - ONE - letter from the alphabet!")
            elif not Inputy.isalpha():
                print("Only letters from the alphabet are allowed!")
            else:
                print("You've already guessed that letter. Do you care to guess again?")
        self.guesses.append(Inputy)
        return Inputy

    def game_over(self):
        """Determine whether there is a win or loss event"""
        if self.missed > 4:
            print("I'm afraid you have run out of guesses. You lose. Better luck next time :)")
            return True
        elif self.active_phrase.check_complete(self.guesses):
            print("Congratulations! You guessed the phrase and won!!! :)")
            return True
        else:
            return False

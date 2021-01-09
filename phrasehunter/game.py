#!/usr/bin/env python3
"""The game module"""
#Phrases were taken from: https://wofanswers.com/phrase
import random
from phrasehunter.phrase import Phrase

class Game:
    """The game class"""
    def __init__(self):
        self.Guess = ''
        self.guesses = []
        self.missed = 0
        self.active_phrase = None
        self.phrases = [
        "ALONE IN A CROWD",
        "WITHIN THE REALM OF POSSIBILITY",
        "YOU READ MY MIND",
        "YOUVE NEVER LOOKED BETTER",
        "ZERO GRAVITY",
            ]

    def start(self):
        """Game instance"""
        self.welcome()
        #Initialise the game phrase:
        self.start_game()
        print(Phrase(self.active_phrase, self.Guess, self.guesses).display())
        while not self.game_over():
            self.Guess = self.get_guess()
            if not Phrase(self.active_phrase, self.Guess, self.guesses).check_letter():
                self.missed += 1
                print(f'\nI\'m sorry. There is no \'{self.Guess}\' in this phrase...\n\n'
                f'You have {5 - self.missed} guess(es) remaining.')
            else:
                print(f'\nVery good! There is a(n) \'{self.Guess}\' in this phrase indeed.\n')
            print(Phrase(self.active_phrase, self.Guess, self.guesses).display())

    def welcome(self):
        print("\nWelcome to Sebastiaan's Phrase Hunters game :)")

    def start_game(self):
        """Assign a random phrase"""
        self.active_phrase = self.get_random_phrase().lower()

    def get_random_phrase(self):
        return random.choice(self.phrases)

    def get_guess(self):
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
        if self.missed > 4:
            print("I'm afraid you have run out of guesses. You lose. Better luck next time :)")
            return True
        elif Phrase(self.active_phrase, self.Guess, self.guesses).check_complete():
            print("Congratulations! You guessed the phrase and won!!! :)")
            return True
        else:
            return False

#!/usr/bin/env python3
"""This module is used to show the (secret phrase)"""

class Phrase:
    phrases = [
        "ALONE IN A CROWD",
        "WITHIN THE REALM OF POSSIBILITY",
        "YOU READ MY MIND",
        "YOUVE NEVER LOOKED BETTER",
        "ZERO GRAVITY",
            ]
    
    """The phrase class"""
    def __init__(self, phrase, Guess, guesses):
        self.phrase = phrase.lower()
        self.guesses = guesses
        self.Guess = Guess

    def display(self):
        Visible = ''
        for letter in self.phrase:
            if letter in self.guesses or letter == ' ':
                Visible += ' ' + letter
            else:
                Visible += ' -'
        return Visible

    def check_letter(self):
        return self.Guess in self.phrase

    def check_complete(self):
        return '-' not in self.display()

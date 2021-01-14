#!/usr/bin/env python3
"""This module is used to show the (secret phrase)"""

class Phrase:
    """The phrase class"""
    def __init__(self, phrase, Guess, guesses):
        self.phrase = phrase.lower()
        self.guesses = guesses
        self.Guess = Guess

    def display(self):
        """Show letters that have been guessed and spaces, show dashes for the rest"""
        Visible = ''
        for letter in self.phrase:
            if letter in self.guesses or letter == ' ':
                Visible += ' ' + letter
            else:
                Visible += ' -'
        return Visible

    def check_letter(self):
        """Validate guess"""
        return self.Guess in self.phrase

    def check_complete(self):
        """Check if all letter have been guessed"""
        return '-' not in self.display()

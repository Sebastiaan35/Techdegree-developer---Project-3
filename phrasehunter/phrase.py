#!/usr/bin/env python3
"""Module for displaying the (partially hidden) phrase and validation"""

class Phrase:
    """The phrase class"""
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def display(self, guesses):
        """Show letters that have been guessed and spaces, show dashes for the rest"""
        Visible = ''
        for letter in self.phrase:
            if letter in guesses or letter == ' ':
                Visible += ' ' + letter
            else:
                Visible += ' -'
        return Visible

    def check_letter(self, Guess):
        """Validate guess"""
        return Guess in self.phrase

    def check_complete(self, guesses):
        """Check if all letter have been guessed"""
        return '-' not in self.display(guesses)

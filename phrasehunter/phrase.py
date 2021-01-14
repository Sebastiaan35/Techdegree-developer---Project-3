#!/usr/bin/env python3
"""This module is used to show the (secret phrase)"""
##from phrasehunter.game import Game

class Phrase:
    """The phrase class"""
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def display(self, guesses):
        """Show letters that have been guessed and spaces, show dashes for the rest"""
        Visible = ''
        for letter in self.phrase:
            if letter in self.guesses or letter == ' ':
                Visible += ' ' + letter
            else:
                Visible += ' -'
        return Visible

    def check_letter(self, Guess):
        """Validate guess"""
        return Guess in self.phrase

    def check_complete(self):
        """Check if all letter have been guessed"""
        return '-' not in self.display()

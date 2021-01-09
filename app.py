#!/usr/bin/env python3
"""A Phrase Hunters game Application conform oop principles by Sebastiaan van Vugt"""
import time
import sys
from phrasehunter.game import Game

if __name__ == '__main__':
    Try = 1
    while Try == 1 or input("Do you want to play again? (y/N): ").lower() == 'y':
        game = Game()
        game.start()
        Try += 1
    print("\nThe game will now exit...\n\n"
        "Thank you for playing Sebastiaan's Phrase Hunters game.")
    time.sleep(2)
    sys.exit()

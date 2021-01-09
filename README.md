This is Project 3 - OOP-phrase-hunter-game - of the Teamtreehouse developer techdegree

Entry for preliminary review
Developed by: Sebastiaan van Vugt
Date: 9.Jan.2021


Copy of instrunctions:
https://teamtreehouse.com/projects/phrase-hunters#instructions


Project Instructions
To complete this project, follow the instructions below. If you get stuck, ask a question on Slack or in the Treehouse Community.

 8 steps
Create the Phrase class in the phrase.py file
The class should include an initializer or def __init__ that receives a phrase parameter and holds this phrase in an instance attribute on the Phrase object.

phrase: this is the actual phrase the Phrase object is representing. This attribute should be set to the phrase parameter but converted to all lower case.
The class should also have these methods:

display(): this prints out the phrase to the console with guessed letters visibile and unguessed letters as underscores. For example, if the current phrase is "hello world" and the user has guessed the letter "o", the output should look like this: _ _ _ _ o    _ o _ _ _
check_letter(): checks to see if the letter selected by the user matches a letter in the phrase.
check_complete(): checks to see if the whole phrase has been guessed.
Create the Game class in the game.py file
The class should include an initializer or def __init__ method that sets the following attributes:

missed: used to track the number of incorrect guesses by the user. The initial value is 0 since no guesses have been made at the start of the game.
phrases: a list of five Phrase objects to use with the game. A phrase should only include letters and spaces -- no numbers, puntuation or other special characters.
active_phrase: This is the Phrase object that's currently in play. The initial value will be None. Within the start_game() method, this property will be set to the Phrase object returned from a call to the get_random_phrase() method.
guesses: This is a list that contains the letters guessed by the user.
The class should also have these methods:

start(): Calls the welcome method, creates the game loop, calls the get_guess method, adds the user's guess to guesses, increments the number of missed by one if the guess is incorrect, calls the game_over method.
get_random_phrase(): this method randomly retrieves one of the phrases stored in the phrases list and returns it.
welcome(): this method prints a friendly welcome message to the user at the start of the game
get_guess(): this method gets the guess from a user and records it in the guesses attribute
game_over(): this method displays a friendly win or loss message and ends the game.
The Game instance might be responsible for things like: starting the game loop, getting player's input() guesses to pass to a Phrase object to perform its responsibilities against, determining if a win/loss happens after the player runs out of turns or the phrase is completely guessed.

Update the app.py file
Import your Game class from the phrasehunter package.
Create a new instance of the Game class and store this instance in a game variable.
Call the start() method you create for your Game instance that kicks off the game loop, this should start the game in the console.
Ensure you place your instance creation and method calls inside a Dunder Main statement.
You must use OOP principles for the entire constructions game meaning no helper functions should be used outside of the classes built above. The entire game should run solely on creating an instance of a Game class and method calls within that instance.

Before the first guess
For each run of the game, a random phrase should be selected from a list of phrases (no punctuation or numbers in phrases and a phrase must be comprised of more than one word).

Before a player has made their first guess, the active phrase should be displayed to the player with underscores as placeholders for the letters. Any spaces between words in the phrase must be clearly visible to the player.

Example: If the phrase "cat in the hat" was selected to be the active phrase. Before the first guess the player would see the phrase displayed with a prompt to guess, such as this:

_ _ _  _ _  _ _ _  _ _ _

Guess a letter:
Prompting for a guess
The game must prompt for the player�s guess on every turn.

Guessing Logic
After every guess, the game should check whether or not the guessed letter is in the active phrase:

After every correct guess, the underscored phrase should be displayed again with any correctly guessed letters in place of the associated underscore.
After every incorrect guess, the number missed should increase by one. The game is over when the user has guessed incorrectly five times.
Example: Correct guess

If the phrase "cat in the hat" was selected to be the active phrase and a correct letter guess of a was made by the player. The console would display as such:

_ _ _  _ _  _ _ _  _ _ _

Guess a letter: a

_ a _  _ _  _ _ _  _ a _

Guess a letter:
Example: Incorrect guess

If the phrase "cat in the hat" was selected to be the active phrase and a correct letter guess of q was made by the player. The console would display as such:

_ _ _  _ _  _ _ _  _ _ _

Guess a letter: q

You have 4 out of 5 lives remaining!

_ _ _  _ _  _ _ _  _ _ _

Guess a letter:
The win or loss state
When the game is over, due to either win or loss, a message must be displayed to the user, and the game must not prompt for another guess.

Before submitting the project
Before you submit your project, check off each item in the project submissions checklist below.

 I have read all of the project instructions, including the �How you�ll be graded� section for this project.

 I understand what is needed to receive a Meets or Exceeds Expectations grade, and asked for clarification about grading requirements on Slack if necessary.

 My GitHub repo for this project contains only this project, only files needed to make this project run, and a README.md file providing details about my project.

 I wrote all of my own code for this project. Any code included in my project that I did not write myself is appropriately attributed to its source.

 I have completed all of the project requirements and believe the project is ready to receive a meets or exceeds expectation grade.

 I have received a preliminary review of my project in Slack to catch anything I might have missed.

 I understand that in order to receive an Exceeds Expectations grade, I must complete all extra credit items.

 I understand that what I submit is what will get reviewed, and that when I submit my project, any changes I make after the submission won't be seen by my reviewer.

Extra Credit
To get an "exceeds" rating, complete all of the steps below:

 2 steps
Validate guesses
If the player inputs more than 1 character, or inputs a character that is not a letter character (a through z). The player should be shown an error message and should be asked to guess again.
NOTE: It is entirely up to you if you want to remove a turn for these types of incorrect guesses.

Multiple games
When the player has reached a win or loss state, the player should be prompted to play again and if the player agrees, a new game is started.
NOTE: This means you must either create and run a NEW game instance or you must have some kind of method that resets all the attributes to defaults such as resetting the stored turns for the player.

NOTE: Getting an "Exceed Expectations" grade.

See the rubric in the "How You'll Be Graded" tab above for details on what you need to receive an "Exceed Expectations" grade.
Passing grades are final. If you try for the "Exceeds Expectations" grade, but miss an item and receive a �Meets Expectations� grade, you won�t get a second chance. Exceptions can be made for items that have been misgraded in review.
Always mention in the comments of your submission or any resubmission, what grade you are going for. Some students want their project to be rejected if they do not meet all Exceeds Expectations Requirements, others will try for all the "exceeds" requirement but do not mind if they pass with a Meets Expectations grade. Leaving a comment in your submission will help the reviewer understand which grade you are specifically going for
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 21:37:56 2022

@author: MD
"""

import random

filename = "sowpods.txt"


class Hangman:
    # Handles an instance of a Hangman game
    def __init__(self):
        # Initialize the variables for the class
        self.endgame = 1 # if endgame == 0 the game ends
        self.words = [] # list of words that can be guessed (read from a file)
        self.word = None # randomly drawn word to be guessed from self.words list
        self.word_hidden = [] # list of letters of word to be guessed changed to underscores if unguessed
        self.line1 = " " # characters divided in 3 lines to print a hangman
        self.line2 = "   " # characters divided in 3 lines to print a hangman
        self.line3 = "   " # characters divided in 3 lines to print a hangman
        self.letter = None # letter guessed by user
        self.guessed = set() # set of already guessed letters
        self.chances = 6 # counter showing the number of chances left
        self.indexes = [] # list of indexes of correctly guessed letter  

    def show_game_name(self):
    # Prints the name of a game at the beginning
        print("\n\n*****************************************")
        print("***************  HANGMAN  ***************")
        print("*****************************************\n")
        print("You have to find out the word by guessing one letter at a time. \
You can have a maximum of 6 incorrect guesses. If you fail, you'll be hanged.\n")    
        
    def read_list_of_words(self):
    # Reads a file and makes it a list
        with open(filename, "r") as f:
            line = f.readline().strip()
            while line:
                self.words.append(line)
                line = f.readline().strip()

    def get_random_word(self):
    # Generates random index and gets the word which is under that index on the
    # self.words list
        self.word = self.words[random.randint(0, len(self.words))]
        
    def print_word_hidden(self):
    # Prints "_" in place of a letter in the randomly chosen word
        for letter in range(0, len(self.word)):
            self.word_hidden.append("_")
        print(" ".join(self.word_hidden))
        
    def print_hangman(self):
    # Prints parts of hangman
        print("\n +---+\n |   |")
        print(f" {self.line1}   |")
        print(f"{self.line2}  |")
        print(f"{self.line3}  |")
        print("     |")
        print("---------\n---------")
                
    def ask_for_letter(self):
    # Gets a letter from a player and checks if it's a single letter. Informs
    # player if not and gets another
        while True:
            self.letter = input("Guess your letter: ")
            if len(self.letter) == 1 and self.letter.isalpha():
                break
            else:
                print("Your input must be one letter!")
            
    def check_letter(self):
    # Checks if a guessed letter is in the word and informs player
        if self.letter.upper() in self.word and self.letter.upper() not in self.guessed:
            print("Correct!")
        elif self.letter.upper() not in self.word and self.letter.upper() not in self.guessed:
            print("Incorrect!")
            
    def get_guessed_letter_index(self):
    # Gets a position(index) of a guessed letter in a word and adds it to a list of indexes
        self.indexes = []    
        for index in range(0,len(self.word)):
                if self.word[index] == self.letter.upper():
                    self.indexes.append(index)
    
    def print_guessed_letters(self):
     # Correctly guesssed letters' indexes indicates positions on which the letter should be printed
        if self.endgame == 1:
            for x in self.indexes:
                self.word_hidden[x] = self.letter.upper()
            print(" ".join(self.word_hidden))
        
    def check_if_game_is_over(self):
    # Checks if the game is over and prints a message to a player
        if "_" not in self.word_hidden:
            print("\nCongratulations! You win!")
            self.endgame = 0
        if self.chances == 0:
            print("\nSorry, you've been hanged!")
            self.endgame = 0
            print("\nThe word is " + self.word.upper())
                
    def save_guessed_letter(self):
        if self.letter.upper() in self.guessed:
            print("That letter was already chosen")
        else:
            self.guessed.add(self.letter.upper())
            
    def count_chances_left(self):
    # Counts how many chances the player has left
        if self.letter.upper() not in self.guessed and self.letter.upper() not in self.word:
            self.chances -= 1

    def print_number_of_chances_left(self):
    # Prints how many incorrect guesses you have left
        if self.endgame == 1:
            print("\nYou have " + str(self.chances) + " chances left")
        
    def ask_about_next_round(self):
    # Asks a player if he wants to play again
        while True:
            try:
                self.endgame = int(input("Do you want to play again? Please enter \"1\" for \"yes\" or \"0\" for \"no\": "))
                if self.endgame == 1 or self.endgame == 0:
                    self.word_hidden = []
                    self.chances = 6
                    self.line1 = " " 
                    self.line2 = "   " 
                    self.line3 = "   "
                    self.guessed = set()
                    break
                else:
                    print("Your input must be either 1 or 0")
            except ValueError:
                print("You must enter a number!")
                
    def add_hangmans_elements(self):
    # Adds hangman's parts one in turn, depending on number of incorrect guesses (chances left)
        if self.chances == 6:
            self.line1 = " "
            self.line2 = "   "
            self.line3 = "   "
        elif self.chances == 5:
            self.line1 = "O"
            self.line2 = "   "
            self.line3 = "   "
        elif self.chances == 4:
            self.line1 = "O"
            self.line2 = "/  "
            self.line3 = "   "
        elif self.chances == 3:
            self.line1 = "O"
            self.line2 = "/| "
            self.line3 = "   "
        elif self.chances == 2:
            self.line1 = "O"
            self.line2 = "/|\\"
            self.line3 = "   "
        elif self.chances == 1:
            self.line1 = "O"
            self.line2 = "/|\\"
            self.line3 = "/  "  
        elif self.chances == 0:
            self.line1 = "O"
            self.line2 = "/|\\"
            self.line3 = "/ \\" 
        
    def simulate(self):
    # Plays rounds of Hangman
        while self.endgame == 1:
            self.show_game_name()
            self.read_list_of_words()
            self.get_random_word()
            self.print_word_hidden()
            self.print_hangman()
            while self.endgame == 1 and self.chances > 0:
                self.ask_for_letter()
                self.check_letter()
                self.get_guessed_letter_index()
                self.count_chances_left()
                self.save_guessed_letter()
                self.print_guessed_letters()
                self.check_if_game_is_over()
                self.add_hangmans_elements()
                self.print_hangman()
                self.print_number_of_chances_left()
            self.ask_about_next_round()


if __name__ == "__main__":
    game = Hangman()
    game.simulate() 
    
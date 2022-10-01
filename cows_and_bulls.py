# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 17:15:38 2022

@author: MD
"""

import random


class CowsAndBulls:
    # Handles an instance of a cows and bulls game
    def __init__(self):
        # Initialize the variables for the class
        self.numbers = [] # list of digits to be guessed
        self.numbers_str = None # digits to be guessed converted to string
        self.guess = "" # 4-digit number guessed by player
        self.bulls = 0 # number of "bulls": digits correctly guessed and in a correct position
        self.cows = 0 # number of "cows": digits correctly guessed but in incorrect position, one cow for one number position  
        self.answers = [] # list of player's guesses
    
    def show_game_name(self):
    # Prints the name of a game at the beginning
        print("\n\n*****************************************")
        print("***********  COWS AND BULLS  ************")
        print("*****************************************\n")
        print("You have to guess a 4-digit number. You get one \'bull\' for every \
correct digit in a correct position and one \'cow\' for every single correct \
digit but in an incorrect position. If you would like to quit, type \'q\'.\n")
    
    def randomly_generate_4_digits(self):
    # Randomly generates 4 digits to be guessed 
        for x in range(0,4):
            self.numbers.append(random.randint(0,9))
            
    def convert_random_digits_to_string(self):
    # Converts list of 4 randomly generated digits to a string
        self.numbers_str = "".join(str(e) for e in self.numbers)    

    def get_players_guess(self):
    # Gets 4 digits from a player and quits the game if player typed 'q'
        while True:
            self.guess = input("Guess a 4-digit number: ")
            if len(self.guess) == 4 and self.guess.isdecimal():
                self.answers.append(self.guess)
                break
            elif self.guess.lower() == "q":
                break
            else:
                print("You must enter a 4-digit number")
                
    def check_bulls(self):
    # Checks how many bulls player got in his guess
        self.bulls = 0
        if self.guess != "q":
            for x in range(0,4):
                if self.numbers_str[x] == self.guess[x]:
                    self.bulls += 1
                
    def check_cows(self):
    # Check how many cows player got in his guess
        numbers = []
        guess = []
        self.cows = 0
        if self.guess != "q":
            for x in range(0,4):
                if self.numbers_str[x] != self.guess[x]:
                    numbers.append(self.numbers_str[x])
                    guess.append(self.guess[x])
            for x in numbers:
                if x in guess:
                    self.cows += 1
                    guess.remove(x)
                
    def print_result(self):
    # Prints how many bulls and cows the player got for his guess and numbers
    # he already guessed
        if self.guess != "q":    
            print(f'Bulls: {self.bulls}, cows: {self.cows}')
            print(", ".join(self.answers))
        
    def congratulate_for_winning(self):
    # Congratulates the player for correctly guessed number
        if self.guess != "q":
            print("It\'s correct! Congratulations!")
            
    def choose_quit_or_play(self):
    # Asks the player if he wants to play again or quit
        if self.guess != "q":
            while True:
                self.guess = input("Do you want to play again? Please enter \
\'p\' if you wan to play or \'q\' if you want to quit: ")
                if self.guess == "q" or self.guess == "p":
                    break
                else:
                    print("Please enter either \'q\' or \'p\'")
        
    def initializes_variables_for_next_game(self):
    # Initializes variables if the player wants to play again
        if self.guess == "p":
            self.numbers = []
            self.numbers_str = None
            self.guess = "" 
            self.bulls = 0 
            self.cows = 0 
            self.answers = []
        
    def simulate(self):
    # Plays a round of cows and bulls game with the computer
        while self.guess.lower() != "q":
            self.show_game_name()
            self.randomly_generate_4_digits()
            self.convert_random_digits_to_string()
            while self.guess != self.numbers_str and self.guess.lower() != "q":
                self.get_players_guess()
                self.check_bulls()
                self.check_cows()
                self.print_result()
            self.congratulate_for_winning()
            self.choose_quit_or_play()
            self.initializes_variables_for_next_game()


if __name__ == "__main__":
    game = CowsAndBulls()
    game.simulate()

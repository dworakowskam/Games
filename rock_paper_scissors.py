# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 16:11:15 2022

@author: MD
"""

import random

options = ["rock", "paper", "scissors"]


class RockPaperScissors:
    # Handles an instance of a Rock-Paper-Scissors game
    def __init__(self):
        # Initialize the variables for the class
        self.computer_choice = None
        self.human_choice = None
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.endgame = 0
        
    def show_game_name(self):
    # Prints the name of a game at the beginning
        print("\n\n*****************************************")
        print("*********  ROCK PAPER SCISSORS  *********")
        print("*****************************************\n")
        print("You have to choose one of the three options, computer does the "
              "same. The rock wins with scissors, scissors wins with paper and "
              "paper wins with rock.\n\n")
            
    def show_options(self):
    # Shows what are the numbered options to choose
        print("Your options are:")
        print("\n".join(f"{count + 1}. {option.title()}" for count, option in enumerate(options)))
    
    def get_computer_choice(self):
    # Chooses a choice randomly from the list of options
        self.computer_choice = random.choice(options)
    
    def get_human_choice(self):
    # Gets human choice by number and checks in the options list if it's rock,
    # paper or scissors as well as checks errors
        while True:    
            try:    
                human_choice = int(input("Enter the number of your choice: "))
                if human_choice >= 1 and human_choice <= 3:
                    self.human_choice = options[human_choice - 1]
                    break
                else:
                    print("Your input must be a number between 1 and 3 inclusive!")
            except ValueError:
                print("You must enter a number!")
    
    def show_choices(self):
    # Print what choice user made and what the computer randomly choose
        print(f"Your choice: {self.human_choice}")
        print(f"Computer's choice: {self.computer_choice}")
        
    def check_who_wins(self, human_beats, human_loses_to):
    # Check if computer's choice was equal to one of the options that human
    # loses to or beats to accordingly to what option was chosen by human and
    # print who wins
        if self.computer_choice == human_loses_to:
            print("COMPUTER WINS!\n")
            self.losses += 1
        elif self.computer_choice == human_beats:
            print("YOU WIN!\n")
            self.wins += 1
            
    def show_result(self):
    # Determines arguments for check_who_wins function depending on human choice
    # and checks if there was a draw
        if self.computer_choice == self.human_choice:
            print("IT'S A DRAW!\n")
            self.draws += 1
        if self.human_choice == "scissors":
            self.check_who_wins("paper", "rock")
        elif self.human_choice == "rock":
            self.check_who_wins("scissors", "paper")
        elif self.human_choice == "paper":
            self.check_who_wins("rock", "scissors")
            
    def show_score(self):
        # Prints current player's score
        print(f"Wins: {self.wins}\nLosses: {self.losses}\nDraws: {self.draws}")
        print("-----------------------------------\n")
        
    def ask_of_continuation(self):
        # Ask player if he wants to play again end exits the game if not
        while True:    
            decision = input("Do you want to play again? Choose \"y\" for \"yes\" or \"n\" for \"no\": ")
            if decision.lower() == "y":
                break
            elif decision.lower() == "n":
                self.endgame = 1
                return self.endgame
                break
            else:
                print("Your input must be \"y\" or \"n\"!")
    
    def simulate(self):
        # Plays a round of Rock paper scissors game with the computer
        self.show_game_name()
        while self.endgame == 0:
            self.show_options()
            self.get_computer_choice()
            self.get_human_choice()
            self.show_choices()
            self.show_result()
            self.show_score()
            self.ask_of_continuation()
                    

if __name__ == "__main__":
    game = RockPaperScissors()
    game.simulate()  
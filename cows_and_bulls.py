# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 17:15:38 2022

@author: MD
"""

import random


class CowsAndBulls:
    # Handles an instance of a Rock-Paper-Scissors game
    def __init__(self):
        # Initialize the variables for the class
        self.numbers = [] # list of numbers to be guessed
        self.guess = None # 4-digit number guessed by player
    
    def show_game_name(self):
    # Prints the name of a game at the beginning
        print("\n\n*****************************************")
        print("***********  COWS AND BULLS  ************")
        print("*****************************************\n")
        print("You have to choose one of the three options, computer does the "
              "same. The rock wins with scissors, scissors wins with paper and "
              "paper wins with rock.\n\n")
    
    def randomly_generate_4_digits(self):
    # Randomly generates 4 digits to be guessed 
        for x in range(0,4):
            self.numbers.append(random.randint(0,9))
#return "".join(str(e) for e in lista)    

    def get_players_guess(self):
    # Gets 4 digits from a player
        while True:
            self.guess = input("Guess a 4-digit number: ")
    
    def simulate(self):
    # Plays a round of cows and bulls game with the computer
        self.show_game_name()
        self.randomly_generate_4_digits()


if __name__ == "__main__":
    game = CowsAndBulls()
    game.simulate()
    
# def generate_number(a = 4):
#     lista = []
#     k = 0
#     while k < a:
#         lista.append(random.randint(0,9))
#         k += 1
#     return "".join(str(e) for e in lista)

# def cows_and_bulls(random_digit, guess):
#     bulls = 0
#     cows = 0
#     lista2 = []
#     lista3 = []
#     for x in range(0,4):
#         if int(random_digit[x]) == int(guess[x]):
#             cows += 1
#             print(cows)
#         elif int(random_digit[x]) != int(guess[x]):
#             lista2.append(int(random_digit[x]))
#             lista3.append(int(guess[x]))
#     for x in lista3:
#         if x in lista2:
#             bulls += 1
#             lista2.remove(x)      
#     return print(cows, "cows, ", bulls, "bulls")   

# if __name__ == "__main__":
    
#     generated_number = generate_number()
#     guess = input("Guess a 4-digit number: ")
#     answers = []
#     answers.append(guess)
        
#     while generated_number != guess:
#         cows_and_bulls(generated_number, guess)
#         print(answers)
#         guess = input("Guess again: ")
#         answers.append(guess)
        
#     print("Guessed! Congratulations!")
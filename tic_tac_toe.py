# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 20:21:14 2022

@author: MD
"""

class Board:
    
    def __init__(self, player):
    # Handles an instance of tic tac toe game
        self.board = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
        self.player = player
        self.win = False
        
    def show_game_name(self):
    # Prints the name of a game at the beginning
        print("\n\n*****************************************")
        print("************* TIC TAC TOE  **************")
        print("*****************************************\n")
        print("You have to put three of your marks in a horizontal, vertical, \
or diagonal row to win. Please enter your coordinates in format row,col, where \
row is the row number and col is the column number you want to place your piece.\n")    
    
    def check_if_win(self):
    # Check if there's a winner and returns True if is and False if not
        for x in range(0,3):
            if self.board[x][0] == self.board[x][1] and \
                self.board[x][1] == self.board[x][2] and \
                    (self.board[x][2] == "X" or self.board[x][2] == "O"):
                self.win = True
                return True  
        for y in range(0,3):
            if self.board[0][y] == self.board[1][y] and \
                self.board[1][y] == self.board[2][y] and \
                    (self.board[2][y] == "X" or self.board[2][y] == "O"):
                self.win = True
                return True
        if self.board[0][0] == self.board[1][1] and \
            self.board[1][1] == self.board[2][2] and \
                (self.board[2][2] == "X" or self.board[2][2] == "O"):
                self.win = True
                return True
        if self.board[0][2] == self.board[1][1] and \
            self.board[1][1] == self.board[2][0] and \
                (self.board[2][0] == "X" or self.board[2][0] == "O"):
                self.win = True
                return True
        return False
    
    def check_if_draw(self):
    # Returns False if there are any "." left and the game isn't over and True
    # if the game is over and there was no winner
        if not self.check_if_win():
            for row in self.board:
                for element in row:
                    if element == ".":
                        return False
            return True
        else:
            return False
        
    def show_board(self):
    # Prints a board of tic tac toe
        print("  1 2 3")
        numberRow = 1
        for row in self.board:
            print(numberRow, end = " ")
            for element in row:
                print(element, end = " ")
            print()
            numberRow += 1
            
    def ask_for_coordinates(self):
    # Asks for coordinates of a place where player wants to put his mark
        while True:
            try:
                self.coordinates = input(f"{self.player}, what is your move? ")
                if len(self.coordinates) == 3 and \
                    0 <= int(self.coordinates.split(",")[0])-1 <= 2 and \
                    0 <= int(self.coordinates.split(",")[1])-1 <= 2:
                    break
                else:
                    print("Your coordinates should be in format row,col (from 1 to 3)!") 
            except ValueError:
                print("Your coordinates should be in format row,col (from 1 to 3)!")                
        
    def transform_coordinates_format_and_numeration(self):
    # Tranforms players input into integer format and list numeration
            self.x = int(self.coordinates.split(",")[0])-1
            self.y = int(self.coordinates.split(",")[1])-1
        
    def check_if_free(self):
    # Returns true if the game position is free and false if isn't
        return self.board[self.x][self.y] == "."
    
    def change_player(self):
    # Changes the player for a round of a game
        if self.player == "O":
            self.player = "X"
        else:
            self.player = "O"
            
    def put_to_board(self):
    # Puts "X" or "O" in a chosen position if the position is free
        if self.check_if_free():
            self.board[self.x][self.y] = self.player
            
    def get_player(self):
    # Returns which player has his turn
        return self.player
    
    def show_game_result(self):
    # Prints out who wins or if there's a draw
        if self.check_if_win():
            if self.get_player() == "X":
                print("O wins!")
            else:
                print("X wins!")
        else:
            print("It's a draw")
    
    def simulate(self):
    # Plays rounds of tic tac toe game
        self.show_game_name()
        self.show_board()
        while (not self.check_if_win()) and (not self.check_if_draw()):
            self.ask_for_coordinates()
            self.transform_coordinates_format_and_numeration()
            self.put_to_board()
            self.show_board()
            self.change_player()
        self.show_game_result()
            
    
if __name__ == "__main__":
    game = Board("O")
    game.simulate()
        



    
        
    
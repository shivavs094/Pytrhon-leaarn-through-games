import tkinter as tk
from  itertools import cycle
from tkinter import font
from  typing import  NamedTuple

import row as row


class Player(NamedTuple):
    label: str
    color: str
    BOARD_SIZE = 3
    DEFAULT_PLAYER = (Player(label="X",color="blue"),Player(label="X",color="blue"))

class Move(NamedTuple):
    row:int
    col:int
    label:str=""

class TicTacToeGame:
    def __int__(self,players=DEAFAULT_PLAYERS,board_size=BOARD_SIZE):
        self._players =cycle(players)
        self.board_size = board_size
        self.current_player = next(self._players)
        self.winner_combo = []
        self._current_move =[]
        self._has_winner = False
        self._winning_comboos=[]
        self._setup_board()

    def process_move(self,move):
        row ,col = move.row,move.col
        self._current_move[row][col]= move
        for combo in self ._winning_comboos:
            results =set(self._current_move[n][m].label for n,m in combo)
            is_win = (len(results)==1) and ("" not in results)
            if is_win:
                self._has_winner= True
                self.winner_combo=combo
                break






    def is_valid_move (self ,move):
        """Return True if move is valid ,and false othewise."""
        row,col = move.row,move.col
        move_was_not_played = self._current_moves[row][col] .label ==""
        no_winner= not self._has_winner
        return no_winner and move_was_not_played


    def _get_winning_combos(self):
        rows = [[(move.row,move.col) for move in row ] for row in self._current_move]
        columns =[list (col) for col in zip(*rows)]
        first_diagonal = [ row [i] for i,row in enumerate(rows) ]
        second_diagonal= [ col [j] for j, col in enumerate(reversed(columns))]
        return rows +columns+[first_diagonal,second_diagonal]
    def _setup_board(self):
        self._current_move=[[Move(row,col) for col in range(self.board_size)] for row in range (self.board_size)]
        self._winning_comboos = self._get_winning_combos


class TicTackToeBoard (tk.Tk):
    def __int__(self):
        super().__int__(tk,TK)
        self.title(" Tic_Tac_Toe")
        self._cells= {}
        self._create_board_display()
        self._create_board_grid()

    def _create_board_display(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)
        self.display = tk.Label(master=display_frame,text="Ready?",font=font.Font(size=28,weight= "bold"))
        self.display.pack()

    def _create_board_grid(self):
        grid_frame =tk.Frame(master=self)
        grid_frame.pack()
        for row in range(3):
            self.rowconfigure(row,weight=1,minsize=75)
            self.columnconfigure(row, weight=1, minsize=75)
            for col in range(3):
                button =tk.Button(master=grid_frame,text=" ",font=font.Font(size=36,weight="bold"),fg="black",width=3,height=2,highlightbackground="lightblue")
                self._cells[button]=(row,col)
                button.grid(row=row,column=col,padx=5,pady=5,sticky="nsew")













def main():
    """"Create thr gsme board and run its main loop"""
    board=TicTackToeBoard()
    board.mainloop()
    
if __name__=="__main__":
    main()
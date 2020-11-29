import pygame
from checkers.constants import *
from checkers.board import Board
class Game:
<<<<<<< Updated upstream
    
    def __init__(self,win):
=======
    """
    def __init__(self, id,board, turn):
        self.ready = False
        self.id = id
        self._init()
        self.board = board
        if turn:
            p1_turn = True
            p2_turn = False
        else:
            p2_turn = True
            p1_turn = False
    """
    def __init__(self, win,id = 0):
        self.ready = False
        self.id = id
        self.win = win
>>>>>>> Stashed changes
        self._init()
        self.win = win
        
        
    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()
        
    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}
        
    def reset(self):
        self._init()
        
        
    def select(self,row,col):
        if self.selected:
            result = self._move(row,col)
            if not result:
                self.selected =None
                self.select(row,col)
        
        piece = self.board.get_piece(row,col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

    def winner(self):
        return self.board.winner()
            
    def _move(self,row,col):
        piece = self.board.get_piece(row,col)
        if self.selected and piece == 0 and (row,col) in self.valid_moves:
            self.board.move(self.selected,row,col)
            skipped = self.valid_moves[(row,col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
<<<<<<< Updated upstream
        
=======

>>>>>>> Stashed changes
        else:
            return False
        
        return True
<<<<<<< Updated upstream
    
    def draw_valid_moves(self,moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win,BLUE,(col* SQUARE_SIZE + SQUARE_SIZE//2,row *SQUARE_SIZE + SQUARE_SIZE//2),15) 
=======

>>>>>>> Stashed changes
    def change_turn(self):
        self.valid_moves = []
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED
<<<<<<< Updated upstream
          
=======

    def connected(self):
        return self.ready
>>>>>>> Stashed changes

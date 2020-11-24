import pygame
from checkers.constants import *
from checkers.board import Board


class Game:

    def __init__(self, gameID):
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('checkers')
        self.ready = False
        self.id = gameID
        self._init()


    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.p1 = RED
        self.p2 = WHITE
        self.p1_turn = True
        self.p2_turn = False
        self.selected = None
        self.board = Board()
        self.turn = self.p1
        self.valid_moves = {}

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

    def winner(self):
        if self.board.winner() == self.p1:
            return self.p1
        elif self.board.winner() == self.p2:
            return self.p2
        else:
            return self.board.winner()

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            # self.change_turn(self.turn)

        else:
            return False

        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE,
                               (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)

    def change_turn(self, player):
        self.valid_moves = []
        if player == 0:
            self.p1_turn = False
            self.turn = self.p2
            self.p2_turn = True
        else:
            self.p2_turn = False
            self.turn = self.p1
            self.p1_turn = True

    def connected(self):
        return self.ready
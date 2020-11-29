import pygame
from checkers.constants import *
from checkers.board import *
from checkers.game import Game
FPS = 60

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('checkers')

def get_row_col_from_mouse(pos):
    x,y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row,col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
<<<<<<< Updated upstream
    
    
    while run:
        clock.tick(FPS)
        #change winning text
        if game.winner() != None:
            print(game.winner())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row,col = get_row_col_from_mouse(pos)
                game.select(row,col)
                
                
        game.update()
=======
    n = Network()
    player = int(n.getP())
    #print("You are player ", player+1)

    while run:
        connected = n.send("connected")
        if connected >= 2:
            clock.tick(FPS)
            '''
            try:
                print("before")
                game.board.updateBoard(n.send("get"))
                print(game)
            except:
                #run = False
                game = Game()
                print("Game could not be fetched")
                #break
            '''
            # change winning text
        # if game.winner() is not None:
            #    print(game.winner())
            turn = n.send("turn")
            #print(turn)
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    run = False
                
                if (player == 1 and game.turn == RED ) or (player == 2 and game.turn == WHITE):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        row, col = get_row_col_from_mouse(pos)
                        game.select(row, col)
                    #game.change_turn(player)
                #yes = n.send("addTurn")
                    arr = n.send(game.board.outputBoard())    
                else:
                    arr = n.send("giveMe")
                    game.board.updateBoard(arr)
            '''
                        if game.connected():
                            try:
                                n.send(game.board.outputBoard())
                            except:
                                print("could not send selected position")
                    
            try:
                n.send("update")
            except Exception as e:
                print("could not update window",e)
                        '''
            game.update()
>>>>>>> Stashed changes
    pygame.quit()
    
main()
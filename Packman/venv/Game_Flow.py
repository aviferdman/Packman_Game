import ReadFiles
import Game_Manager
import Visitor

class Game_Flow (Observable):
    
    def __init__(self):
        
        self.observers = []

    def register (observer):

        self.observers.append(observer)


board = [[]]
board = ReadFiles.read_board()
Game_Manager.start_the_game(board)
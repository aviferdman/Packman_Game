import ReadFiles
import GameUnits
import Visitor
from Visitor import Observable

class Game_Manager(Observable):

    def __init__(self):

        self.observers = []
        self.player = None
        self.board = [[]]
        self.list_movable_pieces = None
        self.list_of_points = None
        self.game_won = False
        self.level = 1

    def register(self, observer):

        self.observers.append(observer)

    def move_as_enemy(self, old_row, old_col, new_row, new_col, board, moving):
        if not board[new_row][new_col].is_enemy():
            temp = moving.last_cell
            moving.last_cell = board[new_row][new_col]
            board[new_row][new_col] = moving
            moving.set_location(new_row, new_col)
            board[old_row][old_col] = temp


    def move_as_player(self, old_row, old_col, new_row, new_col, board, moving, list_of_points):
        cell = board[new_row][new_col]
        if cell.is_point():
            self.list_of_points.remove(cell)
            moving.score += 1
        elif cell.is_bonus():
            moving.power = True
            moving.durantion_of_ability = 10
        board[new_row][new_col] = moving
        moving.set_location(new_row, new_col)
        board[old_row][old_col] = GameUnits.Empty(old_row, old_col)


    def move_unit_to(self, board, moving, destination, list_movable_pieces, list_of_points):
        old_row = moving.get_row()
        old_col = moving.get_col()
        new_row = destination.get_row()
        new_col = destination.get_col()
        if destination.possible_to_step_on_me():

            if moving.is_enemy():
                if not destination.is_player():
                    self.move_as_enemy(old_row, old_col, new_row, new_col, self.board, moving)
                else:
                    if destination.power:
                        self.board[old_row][old_col] = moving.last_cell
                        self.list_movable_pieces.remove(moving)
                    else:
                        destination.is_dead = True

            else:
                if not destination.is_enemy():
                    self.move_as_player(old_row, old_col, new_row, new_col, self.board, moving, self.list_of_points)
                else:
                    if moving.power:
                        self.board[old_row][old_col] = GameUnits.Empty(old_row, old_col)
                        self.board[new_row][new_col] = moving
                        moving.set_location(new_row, new_col)
                        self.list_movable_pieces.remove(destination)
                    else:
                        moving.is_dead = True


    def play(self, board, cell, list_movable_pieces, list_of_points):
        row = cell.get_row()
        col = cell.get_col()
        if cell.able_to_move():
            move = cell.pick_a_move()
            left = self.board[row][col - 1]
            right = self.board[row][col + 1]
            up = self.board[row - 1][col]
            down = self.board[row + 1][col]

            if str(move).__eq__("a"):
                self.move_unit_to(self.board, cell, left, self.list_movable_pieces, self.list_of_points)
            if str(move).__eq__("d"):
                self.move_unit_to(self.board, cell, right, self.list_movable_pieces, self.list_of_points)
            if str(move).__eq__("s"):
                self.move_unit_to(self.board, cell, down, self.list_movable_pieces, self.list_of_points)
            if str(move).__eq__("w"):
                self.move_unit_to(self.board, cell, up, self.list_movable_pieces, self.list_of_points)
        else:
            pass


    def play_game(self, board, list_movable_pieces, list_of_points):

        for piece in list_movable_pieces:
                    self.play(self.board, piece, self.list_movable_pieces, self.list_of_points)


    def init_list_of_movable_pieces(self, board):

        list = []
        for row in self.board:
            for col in row:
                if col.able_to_move():
                    list.append(col)
        return list


    def init_the_player(self, list_movable_pieces):

        for piece in self.list_movable_pieces:
            if piece.is_player():
                return piece

    def init_the_points(self, board):

        list = []
        for row in self.board:
            for col in row:
                if col.is_point():
                    list.append(col)
        return list

    def init_level(self):
        self.board = ReadFiles.read_board(self.level)
        self.list_movable_pieces = self.init_list_of_movable_pieces(self.board)
        self.list_of_points = self.init_the_points(self.board)
        player = self.init_the_player(self.list_movable_pieces)
        self.player = player

    def start_the_game (self):
        self.init_level()
        for o in self.observers:
            o.init_the_game()

        while not self.game_won and not self.player.is_dead :
            for o in self.observers:
                o.print_game(self.board)
            self.play_game(self.board, self.list_movable_pieces, self.list_of_points)
            if not self.list_of_points:
                for o in self.observers:
                    o.print_next_level()
                self.level = self.level + 1
                self.init_level()
                if self.board == [[]]:
                    self.game_won = True

        if not self.game_won:
            for o in self.observers:
                o.print_lose()
        else:
            for o in self.observers:
                o.print_end_game()




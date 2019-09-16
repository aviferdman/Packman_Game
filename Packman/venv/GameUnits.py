import random
import Visitor

moves = {
    "up": "w",
    "down": "s",
    "right": "d",
    "left": "a",
}

cells = {
    "Empty": " ",
    "Point": ".",
    "Bonus": "$",
    "Player": "O",
    "Enemy": "@",
    "Wall": "+",
}

class Cell:

    def __init__(self, row, col):
        self.row = row
        self.col = col


    def is_enemy(self):
        pass

    def set_location(self, new_row, new_col):
        self.row = new_row
        self.col = new_col

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col

    def possible_to_step_on_me(self):
        pass

    def able_to_move(self):
        pass

    def pick_a_move(self):
        pass

    def is_player(self):
        pass

    def is_bonus(self):
        pass

    def is_point(self):
        pass

    def to_string(self):
        return "()"


class Player(Cell):

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.score = 0
        self.durantion_of_ability = 0
        self.power = False
        self.is_dead = False

    def is_enemy(self):
        return False

    def possible_to_step_on_me(self):
        return True

    def able_to_move(self):
        return True

    def pick_a_move(self):
        move = input()
        if self.durantion_of_ability > 0:
            self.durantion_of_ability = self.durantion_of_ability - 1
        elif self.durantion_of_ability == 0:
            self.power = False
        try:
            move = move.lower()[0]
        except:
            pass
        return move

    def set_is_dead(self, is_dead):
        self.is_dead = is_dead

    def is_player(self):
        return True

    def is_point(self):
        return False

    def is_bonus(self):
        return False

    def to_string(self):
        return cells.get("Player")

class Enemy(Cell):

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.last_cell = Empty(row, col)

    def is_enemy(self):
        return True

    def possible_to_step_on_me(self):
        return True

    def able_to_move(self):
        return True

    def pick_a_move(self):
        move = random.randint(0, 3)
        if move.__eq__(0):
            return moves.get("up")
        if move.__eq__(1):
            return moves.get("down")
        if move.__eq__(2):
            return moves.get("left")
        if move.__eq__(3):
            return moves.get("right")

    def is_player(self):
        return False

    def is_point(self):
        return False

    def is_bonus(self):
        return False

    def to_string(self):
        return cells.get("Enemy")


class Wall(Cell):

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def possible_to_step_on_me(self):
        return False

    def able_to_move(self):
        return False

    def is_player(self):
        return False

    def is_point(self):
        return False

    def is_bonus(self):
        return False

    def to_string(self):
        return cells.get("Wall")


class Point(Cell):

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def possible_to_step_on_me(self):
        return True

    def able_to_move(self):
        return False

    def is_player(self):
        return False

    def is_bonus(self):
        return False

    def is_point(self):
        return True

    def to_string(self):
        return cells.get("Point")


class Empty(Cell):

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def possible_to_step_on_me(self):
        return True

    def able_to_move(self):
        return False

    def is_player(self):
        return False

    def is_point(self):
        return False

    def is_bonus(self):
        return False

    def to_string(self):
        return cells.get("Empty")


class Bonus(Cell):

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def possible_to_step_on_me(self):
        return True

    def able_to_move(self):
        return False

    def is_player(self):
        return False

    def is_point(self):
        return False

    def is_bonus(self):
        return True

    def to_string(self):
        return cells.get("Bonus")

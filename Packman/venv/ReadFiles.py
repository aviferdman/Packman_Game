import GameUnits
import Visitor

cells = {
    "Empty": " ",
    "Point": ".",
    "Bonus": "$",
    "Player": "O",
    "Enemy": "@",
    "Wall": "+",
}

def read_board (level):
    board = [[]]
    rows = []
    row = 0
    col = 0

    try:
        packman_file = open("packman"+str(level)+".txt", "r")
        for line in packman_file:
            for char in line:
                if char.__eq__(cells.get("Wall")):
                    cell = GameUnits.Wall(row,col)
                if char.__eq__(cells.get("Point")):
                    cell = GameUnits.Point(row,col)
                if char.__eq__(cells.get("Empty")):
                    cell = GameUnits.Empty(row,col)
                if char.__eq__(cells.get("Player")):
                    cell = GameUnits.Player(row,col)
                if char.__eq__(cells.get("Enemy")):
                    cell = GameUnits.Enemy(row,col)
                if char.__eq__(cells.get("Bonus")):
                    cell = GameUnits.Bonus(row,col)
                rows.append(cell)
                col += 1
            rows.remove(rows[rows.__len__()-1])
            board.append(rows)
            rows = []
            col = 0
            row += 1
        board.remove(board[0])
        packman_file.close()
        return board

    except:
        return board



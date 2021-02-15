import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QDialog

class Fenetre(QWidget):
    def __init__(self, ):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.player = ['X', 'O']
        self.i = 0

        QWidget.__init__(self)
        self.setWindowTitle("Au tour de O")
        self.initUI()

   

    def paintEvent(self, e):
        pass

    def initUI(self):
        grid = QGridLayout(self)

        self.grille = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(3):
            for j in range(3):
                self.grille[i][j] = QPushButton('', self)
                self.grille[i][j].clicked.connect(lambda _, val=(i, j): self.cb(val))
                grid.addWidget(self.grille[i][j], i, j)

        self.setLayout(grid)

    def play(self):
        self.i = (self.i + 1)%2
        return self.player[self.i]


    def cb(self, coords):
        

        i = coords[0]
        j = coords[1]
        self.setWindowTitle("Au tour de "+self.player[self.i])
        play = self.play()
        self.grille[i][j].setText(play)
        self.board[i][j] = play
        check_for_tie(self.board)
        check_if_game_is_won(play, self.board)
        




def check_if_game_is_won (player, board):
    check_alignments (player, lines (board) + columns (board) + diagonals (board))

def check_alignment_for (player, line):
    if line == [player, player, player]:
        game_is_over (player)

def check_alignments (player, candidates):
    for i in range (0, len (candidates)):
        check_alignment_for (player, candidates[i])

def columns (board):
    tboard = [[]] * 3
    for i in range (0, 3):
        tboard[i] = [" "] * 3
    for i in range (0, 3):
        for j in range (0, 3):
            tboard[j][i] = board[i][j]
    return tboard

def lines (board):
    return (board)

def diagonals (board):
    return [
        [ board[0][0], board[1][1], board[2][2] ],
        [ board[2][0], board[1][1], board[0][2] ]
    ]

def count_empty_cells (board):
    c = 0
    for i in range (0, 3):
        for j in range (0, 3):
            if board[i][j] == " ":
                c = c + 1
    return c

def check_for_tie (board):
    if count_empty_cells (board) == 0:
        print ("Egality!")
        sys.exit (0)

def invalid_choice ():
    print ("Coup invalide!")
    sys.exit (0)

def game_is_over (player):
    print (player + " a gagné!")
    sys.exit (0)

if __name__ == "__main__":

    
    app = QApplication.instance() 
    if not app:
        app = QApplication(sys.argv)

        
    fen = Fenetre()
    fen.show()

    sys.exit(app.exec_())

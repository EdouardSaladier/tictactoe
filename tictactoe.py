#
# Le jeu du morpion
#



import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout

#
class Fenetre(QWidget):
    def __init__(self, ):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.player = ['X', 'O']
        self.i = 0

        QWidget.__init__(self)
        self.setWindowTitle("Ma fenetre")
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
        play = self.play()
        self.grille[i][j].setText(play)
        self.board[i][j] = play
        check_for_tie(self.board)
        check_if_game_is_won(play, self.board)
        





# Pour savoir si un joueur a gagnÃ©, on teste les lignes, les colonnes
# et les diagonales de la grille pour vÃ©rifier s'il a un alignement.
def check_if_game_is_won (player, board):
    check_alignments (player, lines (board) + columns (board) + diagonals (board))

# Un alignement est une sÃ©quence des 3 symboles du joueur.
def check_alignment_for (player, line):
    if line == [player, player, player]:
        game_is_over (player)

# On va tester tous les alignements possibles de la grille.
def check_alignments (player, candidates):
    for i in range (0, len (candidates)):
        check_alignment_for (player, candidates[i])

# La fonction suivante renvoie les colonnes du plateau.
def columns (board):
    tboard = [[]] * 3
    for i in range (0, 3):
        tboard[i] = [" "] * 3
    for i in range (0, 3):
        for j in range (0, 3):
            tboard[j][i] = board[i][j]
    return tboard

# La fonction suivante renvoie les lignes du plateau.
def lines (board):
    return (board)

# La fonction suivante renvoie les diagonales du plateau.
def diagonals (board):
    return [
        [ board[0][0], board[1][1], board[2][2] ],
        [ board[2][0], board[1][1], board[0][2] ]
    ]

# "count_empty_cells (board)" compte le nombre de cases vides dans la
# grille.
def count_empty_cells (board):
    # On utilise une variable avec laquelle on va compter le nombre de
    # cases vides au fur Ã  mesure du parcours du plateau.
    c = 0
    # On passe sur toutes les lignes...
    for i in range (0, 3):
        #  ... et sur toutes les colonnes:
        for j in range (0, 3):
            if board[i][j] == " ":
                # Si la case contient un espace alors on la compte comme vide.
                c = c + 1
    # Une fois le parcours du plateau effectuÃ©, le rÃ©sultat est dans "c".
    return c

# La procÃ©dure suivante teste s'il reste encore des cases vides pour jouer.
def check_for_tie (board):
    if count_empty_cells (board) == 0:
        # S'il ne reste plus de case, alors la partie est terminÃ©e sur
        # une Ã©galitÃ©.
        print ("Egality!")
        sys.exit (0)

# La procÃ©dure suivante arrÃªte le programme suite Ã  un coup invalide.
def invalid_choice ():
    print ("Coup invalide!")
    sys.exit (0)

# La procÃ©dure suivante annonce le vainqueur et stoppe le programme.
def game_is_over (player):
    print (player + " a gagné!")
    sys.exit (0)

# Le programme principal
if __name__ == "__main__":

    
    app = QApplication.instance() 
    if not app:
        app = QApplication(sys.argv)

        
    fen = Fenetre()
    fen.show()

    sys.exit(app.exec_())

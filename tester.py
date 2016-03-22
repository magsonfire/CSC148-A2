from grid_peg_solitaire_puzzle import *

g = [["*",".",".","*"],[".",".","*","*"],[".","*",".","."],[".",".",".","."]]

k = GridPegSolitairePuzzle(g,{"*", ".", "#"})
print(k.extensions())


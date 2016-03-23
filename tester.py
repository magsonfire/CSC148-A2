from grid_peg_solitaire_puzzle import *
from puzzle_tools import *

grid = [["*", "*", "*"],
            ["*", "*", "*"],
            [".", "*", "*"]]
gpsp = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
import time

start = time.time()
solution = depth_first_solve(gpsp)
end = time.time()
print("Solved 5x5 peg solitaire in {} seconds.".format(end - start))
print("Using depth-first: \n{}".format(solution))
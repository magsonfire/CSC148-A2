from puzzle import Puzzle


class MNPuzzle(Puzzle):
    """
    An nxm puzzle, like the 15-puzzle, which may be solved, unsolved,
    or even unsolvable.
    """

    def __init__(self, from_grid, to_grid):
        """
        MNPuzzle in state from_grid, working towards
        state to_grid

        @param MNPuzzle self: this MNPuzzle
        @param tuple[tuple[str]] from_grid: current configuration
        @param tuple[tuple[str]] to_grid: solution configuration
        @rtype: None
        """
        # represent grid symbols with letters or numerals
        # represent the empty space with a "*"
        assert len(from_grid) > 0
        assert all([len(r) == len(from_grid[0]) for r in from_grid])
        assert all([len(r) == len(to_grid[0]) for r in to_grid])
        self.n, self.m = len(from_grid), len(from_grid[0])
        self.from_grid, self.to_grid = from_grid, to_grid

    # TODO
    # implement __eq__ and __str__
    # __repr__ is up to you
    def __eq__(self, other):
	    """
		Return whether self is equivalent to other.
		
		@param MNPuzzle self: this MNPuzzle
		@param MNPuzzle|object other: object to compare to self
		@rtype: bool
		
		>>> start = (("*", "2", "3"), ("1", "4", "5"))
		>>> finish = (("1", "2", "3"), ("4", "5", "*"))
		>>> p1 = MNPuzzle(start, finish)
		>>> p2 = MNPuzzle ((("*", "2", "3"), ("1", "4", "5")), (("1", "2", "3"), ("4", "5", "*")))
		>>> p3 = MNPuzzle ((("1", "*", "3"), ("4", "2", "5")), (("1", "2", "3"), ("4", "5", "*")))
		>>> p1 == p2
		True
		>>> p2 == p3
		False
		"""
		pass
	
	def __str__(self):
	    """
		Return a human-friendly representation of MNPuzzle self.
		
		@param MNPuzzle self: this MNPuzzle
		@rtype: str
		"""
		pass
		
	
    # TODO
    # override extensions
    # legal extensions are configurations that can be reached by swapping one
    # symbol to the left, right, above, or below "*" with "*"

    # TODO
    # override is_solved
    # a configuration is solved when from_grid is the same as to_grid


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    target_grid = (("1", "2", "3"), ("4", "5", "*"))
    start_grid = (("*", "2", "3"), ("1", "4", "5"))
    from puzzle_tools import breadth_first_solve, depth_first_solve
    from time import time
    start = time()
    solution = breadth_first_solve(MNPuzzle(start_grid, target_grid))
    end = time()
    print("BFS solved: \n\n{} \n\nin {} seconds".format(
        solution, end - start))
    start = time()
    solution = depth_first_solve((MNPuzzle(start_grid, target_grid)))
    end = time()
    print("DFS solved: \n\n{} \n\nin {} seconds".format(
        solution, end - start))

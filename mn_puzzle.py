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
		
		>>> p1 = MNPuzzle ((("*", "2", "3"), ("1", "4", "5")), (("1", "2", "3"), ("4", "5", "*")))
		>>> print(p1)
		
		* 2 3 
		1 4 5
		=====
		Target:
		=====
		1 2 3
		4 5 *
		
		"""
		current = " "
		    for c in from_grid:
			    row = " ".join(c)
				current += row + "\n"
			current += "=====" + "\n" + "Target:" + \\
			            "=====" + "\n"
			for d in to_grid:
			    row = " ".join(d)
				current += row + "\n"
		return current
	
    # TODO
    # override extensions
    # legal extensions are configurations that can be reached by swapping one
    # symbol to the left, right, above, or below "*" with "*"
    def extensions(self):
	    """
		"""
		#remember position of * by the row it's in and the column it's in
		for row in from_grid:
		    if "*" in row:
			    row_position = from_grid.index(row)
				column_position = row.index("*")
				
		#if the position to the RIGHT of the * does not exist,
		#i.e. the * is in the last column, 
		#i.e. column_position + 1 > length of the row, 
		#then this move to the right does not exist either
		#so if column_position + 1 < length of the row,
		#start building the tuple that would make up the 'from_grid' parameter in the MNPuzzle init method
		if column_position + 1 < len(from_grid[0]):
		    
			#copy all the rows above the row containing *
			#i.e. copy all the rows from from_grid[0] up to but not including from_grid[row_position]
			#then need to reconstruct the row (which is a tuple) containing * 
			#with the * swapped with the symbol at column_position + 1
			#need to put in if/else condition for when the * ends up being swapped into the last column
			#or will get an error
			#i.e. can't call from_grid[row_position][column_position + 2:] because index not in range
			#then finish up by copying in all the rows after the row containing *
		    next_grid = (from_grid[:row_position], (from_grid[row_position][:column_position], \\
			                                        from_grid[row_position][column_position + 1], \\
													"*", \\
			                                        from_grid[row_position][column_position + 2:] if column_position + 2 else pass), \\
													from_grid[row_position + 1:])
			#finally create the MNPuzzle object with the configuration of having moved the * to the right
			#this possible configuration will be added to a list at the end after having
			#created all the other possible extensions
		    move_right = MNPuzzle(next_grid, to_grid)
		
		#if the * is not located in the first column, then the possibility
		#to move * to the left exists
		if column_position - 1 > 0:
		    next_grid = (from_grid[:row_position], (from_grid[row_position][:column_position - 1] if column_position - 1 > 0 else pass, \\
			                                        "*", \\
													from_grid[row_position][column_position - 1], \\
													from_grid[row_position][column_position:]), \\
													from_grid[row_position + 1:])
			move_left = MNPuzzle(next_grid, to_grid)
		if row_position > 0:   
		    next_grid = (from_grid[:row_position - 1], (from_grid[row_position - 1][:column_position], "*", from_grid[row_position - 1][column_position + 1:]), \\
			    ()

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

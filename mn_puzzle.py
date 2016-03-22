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

    # implement __eq__ and __str__
    # __repr__ is up to you
    def __eq__(self, other):
        """
        Return whether self is equivalent to other.

        @param MNPuzzle self: this MNPuzzle
        @param MNPuzzle | object other: object to compare self to
        @rtype: bool

        >>> start = (("*", "2", "3"), ("1", "4", "5"))
        >>> finish = (("1", "2", "3"), ("4", "5", "*"))
        >>> p1 = MNPuzzle(start, finish)
        >>> p2 = MNPuzzle ((("*", "2", "3"), ("1", "4", "5")), finish)
        >>> p3 = MNPuzzle ((("1", "*", "3"), ("4", "2", "5")), finish)
        >>> p1 == p2
        True
        >>> p2 == p3
        False
        """
        return (type(self) == type(other) and
                (self.from_grid == other.from_grid) and
                (self.to_grid == other.to_grid))

    def __str__(self):
        """
        Return a human-friendly representation of MNPuzzle self.

        @param MNPuzzle self: this MNPuzzle
        @rtype: str

        >>> start = (("*", "2", "3"), ("1", "4", "5"))
        >>> finish = (("1", "2", "3"), ("4", "5", "*"))
        >>> p1 = MNPuzzle(start, finish)
        >>> print(p1)
        * 2 3
        1 4 5
        =====
        Target:
        =====
        1 2 3
        4 5 *
        """
        current = ""
        for c in self.from_grid:
            row1 = ""
            for ch in c:
                row1 += ch + " "
            current += row1.rstrip() + "\n"
        current += "=====" + "\n" + "Target:\n" + "=====" + "\n"
        for d in self.to_grid:
            row2 = " ".join(d)
            current += row2.rstrip() + "\n"
        return current.rstrip()

    # TODO
    # override extensions
    # legal extensions are configurations that can be reached by swapping one
    # symbol to the left, right, above, or below "*" with "*"

    def extensions(self):
        """
        Return a list of possible configurations one step away from the current
        configuration.

        >>> start = (("2", "*", "3"), ("1", "4", "5"))
        >>> finish = (("1", "2", "3"), ("4", "5", "*"))
        >>> right = MNPuzzle((("2", "3", "*"), ("1", "4", "5")), finish)
        >>> left = MNPuzzle((("*", "2", "3"), ("1", "4", "5")), finish)
        >>> down = MNPuzzle((("2", "4", "3"), ("1", "*", "5")), finish)
        >>> p1 = MNPuzzle(start, finish)
        >>> p1.extensions() == [right, left, down]
        True
        """
        start = self.from_grid
        for row in start:
            if "*" in row:
                row_pos = start.index(row)
                col_pos = row.index("*")
        if row_pos == 0 and col_pos == 0:
            return [self.move_right(), self.move_down()]
        if row_pos == 0 and col_pos == len(start[0]) - 1:
            return [self.move_left(), self.move_down()]
        if row_pos == len(start) - 1 and col_pos == 0:
            return [self.move_right(), self.move_up()]
        if row_pos == len(start) - 1 and col_pos == len(start[0]) - 1:
            return [self.move_left(), self.move_up()]
        if row_pos == 0:
            return [self.move_right(), self.move_left(), self.move_down()]
        if row_pos == len(start) - 1:
            return [self.move_right(), self.move_left(), self.move_up()]
        if col_pos == 0:
            return [self.move_right(), self.move_down(), self.move_up()]
        if col_pos == len(start[0]) - 1:
            return [self.move_left(), self.move_down(), self.move_up()]
        else:
            return [self.move_right(), self.move_left(), self.move_up(), self.move_down()]

    #helper functions
    def move_left(self):
        """
        Return configuration of self when "*" is swapped with the element to the
        left of "*".

        >>> start = (("2", "*", "3"), ("1", "4", "5"))
        >>> finish = (("1", "2", "3"), ("4", "5", "*"))
        >>> p1 = MNPuzzle(start, finish)
        >>> p1.move_left() == MNPuzzle((("*", "2", "3"), ("1", "4", "5")), finish)
        True
        """
        
        start = self.from_grid
        end = self.to_grid
        grid_list = []
        #create list of str of all elements in grid
        for row in start:
            for x in row:
                grid_list.append(x)
        #remember position of * by row pos and col pos
        row_pos = grid_list.index("*")
        #swap * with symbol to its left
        grid_list[row_pos] = grid_list[row_pos - 1]
        grid_list[row_pos - 1] = "*"
        #create new list to put in all new tuples of rows
        final = []
        #but first create tuples of appropriate length; start with index 0 and
        i = 0
        while i < len(grid_list):
            #and fill each tuple with appropriate number of elements (row length)
            a = tuple(grid_list[i:i + len(start[0])])
            #add each tuple (i.e. row) to the final list as it is created
            final.append(a)
            #increment i by row length and create tuple for next row
            i += len(start[0])
        #return the tuple version of the final list of all the rows in grid
        return MNPuzzle(tuple(final), end)
            

    def move_right(self):
        """
        Return configuration of self when "*" is swapped with the element
        to the right of "*".

        >>> start = (("2", "*", "3"), ("1", "4", "5"))
        >>> finish = (("1", "2", "3"), ("4", "5", "*"))
        >>> p1 = MNPuzzle(start, finish)
        >>> p1.move_right() == MNPuzzle((("2", "3", "*"), ("1", "4", "5")), finish)
        True

        """
        start = self.from_grid
        end = self.to_grid
        grid_list = []
        for row in start:
            for x in row:
                grid_list.append(x)
        row_pos = grid_list.index("*")
        #swap * with symbol to its right
        grid_list[row_pos] = grid_list[row_pos + 1]
        grid_list[row_pos + 1] = "*"
        final = []
        i = 0
        while i < len(grid_list):
            a = tuple(grid_list[i:i + len(start[0])])
            final.append(a)
            i += len(start[0])
        return MNPuzzle(tuple(final), end)
    

    def move_up(self):
        """
        Return the configuration of self when "*" is swapped with the element
        above the "*".

        >>> start = (("2", "4", "3"), ("1", "*", "5"))
        >>> finish = (("1", "2", "3"), ("4", "5", "*"))
        >>> p1 = MNPuzzle(start, finish)
        >>> p1.move_up() == MNPuzzle((("2", "*", "3"), ("1", "4", "5")), finish)
        True
        """
        start = self.from_grid
        end = self.to_grid
        grid_list = []
        for row in start:
            for x in row:
                grid_list.append(x)
        row_pos = grid_list.index("*")
        #swap * with symbol that would be above * in grid configuration
        #i.e. swap * with the symbol len(start[0]) places before *
        grid_list[row_pos] = grid_list[row_pos - len(start[0])]
        grid_list[row_pos - len(start[0])] = "*"
        final = []
        i = 0
        while i < len(grid_list):
            a = tuple(grid_list[i:i + len(start[0])])
            final.append(a)
            i += len(start[0])
        return MNPuzzle(tuple(final), end)

    def move_down(self):
        """
        Return the configuration of self when "*" is swapped with the element
        below the "*".

        >>> start = (("2", "*", "3"), ("1", "4", "5"))
        >>> finish = (("1", "2", "3"), ("4", "5", "*"))
        >>> p1 = MNPuzzle(start, finish)
        >>> p1.move_down() == MNPuzzle((("2", "4", "3"), ("1", "*", "5")), finish)
        True
        """
        start = self.from_grid
        end = self.to_grid
        grid_list = []
        for row in start:
            for x in row:
                grid_list.append(x)
        row_pos = grid_list.index("*")
        #swap * with symbol that would be below * in grid configuration
        #i.e. swap * with the symbol len(start[0]) places after *
        grid_list[row_pos] = grid_list[row_pos + len(start[0])]
        grid_list[row_pos + len(start[0])] = "*"
        final = []
        i = 0
        while i < len(grid_list):
            a = tuple(grid_list[i:i + len(start[0])])
            final.append(a)
            i += len(start[0])
        return MNPuzzle(tuple(final), end)


        
           
    # TODO
    # override is_solved
    # a configuration is solved when from_grid is the same as to_grid
    def is_solved(self):
        """
        Return whether the puzzle self is solved or not.

        @param MNPuzzle self: this MNPuzzle
        @rtype: bool

        >>> start = (("2", "*", "3"), ("1", "4", "5"))
        >>> finish = (("1", "2", "3"), ("4", "5", "*"))
        >>> p1 = MNPuzzle(start, finish)
        >>> p1.is_solved()
        False
        >>> start = (("1", "2", "3"), ("4", "5", "*"))
        >>> p2 = MNPuzzle(start, finish)
        >>> p2.is_solved()
        True
        
        """
        return self.from_grid == self.to_grid

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

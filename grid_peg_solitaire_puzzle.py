from puzzle import Puzzle


class GridPegSolitairePuzzle(Puzzle):
    """
    Snapshot of peg solitaire on a rectangular grid. May be solved,
    unsolved, or even unsolvable.
    """

    def __init__(self, marker, marker_set):
        """
        Create a new GridPegSolitairePuzzle self with
        marker indicating pegs, spaces, and unused
        and marker_set indicating allowed markers.

        @type marker: list[list[str]]
        @type marker_set: set[str]
                          "#" for unused, "*" for peg, "." for empty
        """
        assert isinstance(marker, list)
        assert len(marker) > 0
        assert all([len(x) == len(marker[0]) for x in marker[1:]])
        assert all([all(x in marker_set for x in row) for row in marker])
        assert all([x == "*" or x == "." or x == "#" for x in marker_set])
        self._marker, self._marker_set = marker, marker_set

    # TODO
    # implement __eq__, __str__ methods
    # __repr__ is up to you

    def extensions(self):
    # legal extensions consist of all configurations that can be reached by
    # making a single jump from this configuration
        #helper function to find Pegs
        def find_peg(row):
            for row in self._marker:
                for x in row:
                    star_index = []
                    if x.value == '*':
                        star_index = x.index

        def get_position(x,y):
            #check if X and Y are in the proper bounds
            if x > 0 and x <= len(self._marker) and y > 0 and y <= len(self._marker[0]):
                return self._marker[x-1][y-1]
            else:
                return None

        def check_right(x,y):
            return get_position(x+1,y) == "*" and get_position(x+2,y) == '.'

        def move_right(x,y):
            new_config = self._marker[:]
            new_config[x] = '.'
            new_config[x+1] = '.'
            new_config[x+2] = '*'
            return GridPegSolitairePuzzle(new_config, self._marker_set)

    def is_solved(self):
        star_count = 0
        #going through the rows to count *
        for row in self._marker:
            star_count += row.count('*')
            #total stars should not exceed 1
            if star_count >= 1:
                return False

        return True

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    from puzzle_tools import depth_first_solve

    grid = [["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"],
            ["*", "*", ".", "*", "*"],
            ["*", "*", "*", "*", "*"]]
    gpsp = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
    import time

    start = time.time()
    solution = depth_first_solve(gpsp)
    end = time.time()
    print("Solved 5x5 peg solitaire in {} seconds.".format(end - start))
    print("Using depth-first: \n{}".format(solution))

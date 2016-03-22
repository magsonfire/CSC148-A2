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

    # implement __eq__, __str__ methods
    def __eq__(self, other):

        return(type(other) == type(self) and
               self._marker == other._marker and
               self._marker_set == other._marker_set)

    def __str__(self):
        for r in self._marker:
            for c in self._marker:
                print('row {} : {} coloumn {} : {}').format(r,self._marker[r],c,self._marker[c])

    # __repr__ is up to you

    def extensions(self):
    # legal extensions consist of all configurations that can be reached by
    # making a single jump from this configuration

        #helper function to find Pegs
        def find_peg(marker):
            peg_locations = []
            for r in range(len(marker)):
                for c in range(len(marker[r])):
                    if marker[r][c] == '*':
                        peg_locations.append((r,c))

            return peg_locations

        def get_position(r,c):
            #check if R and C are in the proper bounds
            if r >= 0 and r < len(self._marker) and c >= 0 and c < len(self._marker[0]):
                return self._marker[r][c]
            else:
                return None

        def check_right(r,c):
            return get_position(r,c+1) == "*" and get_position(r,c+2) == '.'

        def move_right(r,c):
            new_config = self._marker[:]
            new_config[r][c] = '.'
            new_config[r][c+1] = '.'
            new_config[r][c+2] = '*'
            return GridPegSolitairePuzzle(new_config, self._marker_set)

        def check_left(r,c):
            return get_position(r,c-1) == "*" and get_position(r,c-2) =='.'

        def move_left(r,c):
            new_config = self._marker[:]
            new_config[r][c] ='.'
            new_config[r][c-1] = '.'
            new_config[r][c-2] = '*'
            return GridPegSolitairePuzzle(new_config,self._marker_set)

        def check_up(r,c):
            return get_position(r-1, c) == '*' and get_position(r-2,c) == '.'

        def move_up(r,c):
            new_config = self._marker[:]
            new_config[r][c] ='.'
            new_config[r-1][c] = '.'
            new_config[r-2][c] = '*'
            return GridPegSolitairePuzzle(new_config,self._marker_set)

        def check_down(r,c):
            return get_position(r+1, c) == '*' and get_position(r+2,c) == '.'

        def move_down(r,c):
            new_config = self._marker[:]
            new_config[r][c] ='.'
            new_config[r+1][c] = '.'
            new_config[r+2][c] = '*'
            return GridPegSolitairePuzzle(new_config,self._marker_set)

        possible_extensions = []

        for peg in find_peg(self._marker):
            if check_right(peg[0],peg[1]):
                possible_extensions.append(move_right(peg[0],peg[1]))

            if check_left(peg[0],peg[1]):
                possible_extensions.append(move_left(peg[0],peg[1]))

            if check_up(peg[0],peg[1]):
                possible_extensions.append(move_up(peg[0],peg[1]))

            if check_down(peg[0],peg[1]):
                possible_extensions.append(move_down(peg[0],peg[1]))

        return possible_extensions

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

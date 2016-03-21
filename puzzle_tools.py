"""
Some functions for working with puzzles
"""
from puzzle import Puzzle
from word_ladder_puzzle import WordLadderPuzzle
from collections import deque
# set higher recursion limit
# which is needed in PuzzleNode.__str__
# uncomment the next two lines on a unix platform, say CDF
# import resource
# resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
import sys
sys.setrecursionlimit(10**6)


# TODO
# implement depth_first_solve
# do NOT change the type contract
# you are welcome to create any helper functions
# you like
def depth_first_solve(puzzle):
    """
    Return a path from PuzzleNode(puzzle) to a PuzzleNode containing
    a solution, with each child containing an extension of the puzzle
    in its parent.  Return None if this is not possible.

    @type puzzle: Puzzle
    @rtype: PuzzleNode
    """
    # return none if unsolvable puzzle
    if puzzle.fail_fast():
        return None

    # from starting configuration, perform depth-first search for solution
    start = PuzzleNode(puzzle, [PuzzleNode(c) for c in puzzle.extensions()]) \
        if puzzle.extensions() != [] else PuzzleNode(puzzle)
    return depth_first_search(start)


def add_children(pn):
    """
    Add PuzzleNode children to a given PuzleNode pn.

    @type puzzle: Puzzle
    @type parent: PuzzleNode
    @rtype: PuzzleNode

    >>> a = WordLadderPuzzle("save", "same", {"same", "save"})
    >>> print(get_puzzle_node(a))
    WordLadderPuzzle(save -> same)
    <BLANKLINE>
    WordLadderPuzzle(same -> same)
    <BLANKLINE>
    <BLANKLINE>
    >>> b = WordLadderPuzzle("same", "same", {"same"})
    >>> print(get_puzzle_node(b))
    WordLadderPuzzle(same -> same)
    <BLANKLINE>
    <BLANKLINE>
    """
    pn.children = pn.puzzle.extensions() if pn.puzzle.extensions() else pass


def depth_first_search(node):
    """
    Return a set of PuzzleNodes traversed in the process of finding a solution
    to the puzzle configuration contained in PuzzleNode node.

    @type node: PuzzleNode
    @rtype: set{PuzzleNode}
    """
    visited = {}
    # initialize deque as FIFO stack (mimicking system call stack)
    to_crawl = deque(node)

    # pop current node being crawled
    node = to_crawl.pop()
    if node.children:
        for c in node.children:
            # add child to stack
            to_crawl.append(c)

    # graph crawl iteration code taken from: [source]
    # before stack is empty (i.e. nodes left to visit)
    while to_crawl:
        if node not in visited:
            visited.add(node)
            # exit function and return visited nodes if solution found
            if node.puzzle.is_solved():
                return visited[0]
        node = deque.pop()
    return visited[0]

# TODO
# implement breadth_first_solve
# do NOT change the type contract
# you are welcome to create any helper functions
# you like
# Hint: you may find a queue useful, that's why
# we imported deque
def breadth_first_solve(puzzle):
    """
    Return a path from PuzzleNode(puzzle) to a PuzzleNode containing
    a solution, with each child PuzzleNode containing an extension
    of the puzzle in its parent.  Return None if this is not possible.

    @type puzzle: Puzzle
    @rtype: PuzzleNode
    """


# Class PuzzleNode helps build trees of PuzzleNodes that have
# an arbitrary number of children, and a parent.
class PuzzleNode:
    """
    A Puzzle configuration that refers to other configurations that it
    can be extended to.
    """

    def __init__(self, puzzle=None, children=None, parent=None):
        """
        Create a new puzzle node self with configuration puzzle.

        @type self: PuzzleNode
        @type puzzle: Puzzle | None
        @type children: list[PuzzleNode]
        @type parent: PuzzleNode | None
        @rtype: None
        """
        self.puzzle, self.parent = puzzle, parent
        if children is None:
            self.children = []
        else:
            self.children = children[:]

    def __eq__(self, other):
        """
        Return whether PuzzleNode self is equivalent to other

        @type self: PuzzleNode
        @type other: PuzzleNode | Any
        @rtype: bool

        >>> from word_ladder_puzzle import WordLadderPuzzle
        >>> pn1 = PuzzleNode(WordLadderPuzzle("on", "no", {"on", "no", "oo"}))
        >>> pn2 = PuzzleNode(WordLadderPuzzle("on", "no", {"on", "oo", "no"}))
        >>> pn3 = PuzzleNode(WordLadderPuzzle("no", "on", {"on", "no", "oo"}))
        >>> pn1.__eq__(pn2)
        True
        >>> pn1.__eq__(pn3)
        False
        """
        return (type(self) == type(other) and
                self.puzzle == other.puzzle and
                all([x in self.children for x in other.children]) and
                all([x in other.children for x in self.children]))

    def __str__(self):
        """
        Return a human-readable string representing PuzzleNode self.

        # doctest not feasible.
        """
        return "{}\n\n{}".format(self.puzzle,
                                 "\n".join([str(x) for x in self.children]))

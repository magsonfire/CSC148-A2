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
    in its parent. Return None if this is not possible.

    @type puzzle: Puzzle
    @rtype: PuzzleNode
    """
    # return none if unsolvable puzzle
    if puzzle.fail_fast():
        return None

    visited = set()
    nodes = []
    # until all extensions from starting config are exhausted
    while not all([str(puzzle.extensions())]) in visited:
        depth_first_search(puzzle, visited, nodes)

    # solution_node should be last node visited
    solution_node = nodes[-1]
    return get_path(solution_node)


def depth_first_search(start, visited, nodes, parent=None):
    """
    Search for a PuzzleNode containing the solution to the configuration in
    PuzzleNode start.

    @type start: Puzzle
    @type visited: set{str}
    @type nodes: list[PuzzleNode]
    @type parent: PuzzleNode | None
    @rtype: None
    """
    # if leaf node, return to last branching point to continue search
    if not start:
        return
    elif start.__str__() in visited:
        pass
    elif start.is_solved():
        return
    else:
        visited.add(start.__str__())
        nodes.append(get_node(start, parent))
        for ext in start.extensions():
            depth_first_search(ext, visited, nodes, start)


def get_node(puzzle, parent=None):
    """
    Return a PuzzleNode from puzzle puzzle, with parent parent.

    @type puzzle: Puzzle
    @type parent: PuzzleNode | None
    @rtype: PuzzleNode
    >>> a = WordLadderPuzzle("save", "same", {"same", "save"})
    >>> print(get_node(a))
    WordLadderPuzzle(save -> same)
    <BLANKLINE>
    WordLadderPuzzle(same -> same)
    <BLANKLINE>
    <BLANKLINE>
    >>> b = WordLadderPuzzle("same", "same", {"same"})
    >>> print(get_node(b))
    WordLadderPuzzle(same -> same)
    <BLANKLINE>
    <BLANKLINE>
    """
    new_node = PuzzleNode(puzzle)
    if puzzle.extensions():
        new_node.children = [PuzzleNode(c) for c in puzzle.extensions()]
    if parent:
        new_node.parent = parent
    return new_node


def get_path(solution_node):
    """
    Return the first node in a doubly-linked list of PuzzleNodes from the
    starting configuration to the PuzzleNode solution_node.

    @type solution_node: PuzzleNode
    @type visited: list[PuzzleNode]
    @rtype: PuzzleNode
    """
    current = solution_node
    # until at the root of the path (no parent)
    while current.parent:
        # walk over each node in doubly-linked list from solution_node
        current = current.parent
    return current



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

    q = deque()
    start = PuzzleNode(puzzle)

    q.append(start)
    tried_ext = []
    while q:
        node = q.popleft()
        # this returns error code 'Puzzle" object has no attribute 'puzzle' :(
        children = node.puzzle.extensions()
        for ext in children:
            if ext not in tried_ext:
                puzzle_node = PuzzleNode(ext)
                puzzle_node.parent = node
                node.children.append(puzzle_node)
                if not ext.is_solved():
                    q.append(ext)
                    tried_ext.append(ext)
                else:
                    final = []
                    cur_node = ext
                    while cur_node:
                        final.append(cur_node)
                        cur_node = ext.parent
                    return final.reverse()
    return None


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

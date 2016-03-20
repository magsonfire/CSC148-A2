from puzzle import Puzzle


class WordLadderPuzzle(Puzzle):
    """
    A word-ladder puzzle that may be solved, unsolved, or even unsolvable.
    """

    def __init__(self, from_word, to_word, ws):
        """
        Create a new word-ladder puzzle with the aim of stepping
        from from_word to to_word using words in ws, changing one
        character at each step.

        @type from_word: str
        @type to_word: str
        @type ws: set[str]
        @rtype: None
        """
        (self._from_word, self._to_word, self._word_set) = (from_word,
                                                            to_word, ws)
        # set of characters to use for 1-character changes
        self._chars = "abcdefghijklmnopqrstuvwxyz"

    def __eq__(self, other):
        """
        Return whether WordLadderPuzzle self is equal to WordLadderPuzzle
        other.

        @type self: WordLadderPuzle
        @type other: WordLadderPuzzle
        @rtype: bool

        >>> word_set = {"safe", "same", "save"}
        >>> a = WordLadderPuzzle("safe", "same", word_set)
        >>> b = WordLadderPuzzle("safe", "same", word_set)
        >>> a == b
        True
        >>> c = WordLadderPuzzle("save", "same", word_set)
        >>> a == c
        False
        """
        return type(self) is type(other) and \
               self._from_word == other._from_word and \
               self._to_word == other._to_word and \
               self._word_set == other._word_set and \
               self._chars == other._chars

    def __str__(self):
        """
        Return a user-friendly string interpretation of WordLadderPuzzle
        self.

        @type self: WordLadderPuzzle
        @rtype: str

        >>> word_set = {"safe", "same", "save"}
        >>> a = WordLadderPuzzle("safe", "same", word_set)
        >>> print(a)
        WordLadderPuzzle(safe -> same)
        """
        return "WordLadderPuzzle({} -> {})".format(self._from_word,
                                                   self._to_word)

    def __repr__(self):
        """
        Return a string representation of WordLadderPuzzle self that can
        be used to recreate the WordLadderPuzzle.

        @type self: WordLadderPuzzle
        @rtype: str

        >>> word_set = {"safe", "same", "save"}
        >>> a = WordLadderPuzzle("safe", "same", word_set)
        >>> a2 = eval(a.__repr__())
        >>> a == a2
        True
        """
        return "WordLadderPuzzle('{}', '{}', {})".format(self._from_word,
                                                     self._to_word,
                                                     self._word_set)

    def extensions(self):
        """
        Return list of extensions of WordLadderPuzzle self.

        @type self: WordLadderPuzzle
        @rtype: list[WordLadderPuzzle]

        >>> word_set = {"safe", "same", "rave"}
        >>> a = WordLadderPuzzle("safe", "same", word_set)
        >>> L1 = list(a.extensions())
        >>> L2 = [WordLadderPuzzle("same", "same", word_set)]
        >>> len(L1) == len(L2)
        True
        >>> all([s in L1 for s in L2])
        True
        >>> all([s in L2 for s in L1])
        True
        """
        # convenient names
        start, end, ws, chars = self._from_word, self._to_word, \
                                self._word_set, self._chars
        # if puzzle is complete, return an empty list
        if start == end:
            return []
        else:
            list_ = []
            # change each letter of start to form a new word
            for i in range(len(start) - 1):
                for char in chars:
                    new_start = start[:i] + char + start[i + 1:]
                    # if new word is a legal word (and not the same as start)
                    if new_start in ws and new_start != start:
                        # add new word as extension of puzzle config
                        list_.append(WordLadderPuzzle(new_start, end, ws))
            return list_

    def is_solved(self):
        """
        Return whether WordLadderPuzzle self is solved.

        @type self: WordLadderPuzzle
        @rtype: bool

        >>> word_set = {"safe", "same", "rave"}
        >>> a = WordLadderPuzzle("safe", "same", word_set)
        >>> a.is_solved()
        False
        >>> b = WordLadderPuzzle("same", "same", word_set)
        >>> b.is_solved()
        True
        """
        # Check that from and to word are the same and that both are legal words
        return self._from_word == self._to_word and \
               (self._from_word and self._from_word) in self._word_set


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    from puzzle_tools import breadth_first_solve, depth_first_solve
    from time import time
    with open("words", "r") as words:
        word_set = set(words.read().split())
    w = WordLadderPuzzle("same", "cost", word_set)
    start = time()
    sol = breadth_first_solve(w)
    end = time()
    print("Solving word ladder from same->cost")
    print("...using breadth-first-search")
    print("Solutions: {} took {} seconds.".format(sol, end - start))
    start = time()
    sol = depth_first_solve(w)
    end = time()
    print("Solving word ladder from same->cost")
    print("...using depth-first-search")
    print("Solutions: {} took {} seconds.".format(sol, end - start))

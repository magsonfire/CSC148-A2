from container import Container

# M: this subclass inherits __eq__ and __str__ classes from Container class

class Stack(Container):
    """
    Last-in, first-out (LIFO) stack.
    """

    def __init__(self):
        """
        Create a new, empty Stack self.

        @param Stack self: this stack
        @rtype: None
        """

        self._contents = []

    def add(self, obj):
        """
        Add object obj to top of Stack self.

        @param Stack self: this Stack
        @param Any obj: object to place on Stack
        @rtype: None


        >>> s = Stack()
        >>> s.add(8)
        >>> s.add(9)
        >>> s
        8, 9
        """

        self._contents.append(obj)

    def remove(self):
        """
        Remove and return top element of Stack self.

        Assume Stack self is not empty.

        @param Stack self: this Stack
        @rtype: object

        >>> s = Stack()
        >>> s.add(5)
        >>> s.add(7)
        >>> s.remove()
        7
        """

        self._contents.pop()

    def is_empty(self):
        """
        Return whether Stack self is empty.

        @param Stack self: this Stack
        @rtype: bool
        """

        return len(self._contents) == 0


if __name__ == "__main__":
    import doctest
    doctest.testmod()

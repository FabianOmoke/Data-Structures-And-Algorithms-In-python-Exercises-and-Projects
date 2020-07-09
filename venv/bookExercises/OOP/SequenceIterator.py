class SequenceIterator:
    """An iterator for any of python's Sequence types"""

    def __init__(self, sequence):
        """Create an iterator for the given sequence"""
        self._seq = sequence     #keep a reference for the underlying data
        self._k = -1             #will increment to 0 on first call to next

    def __next__(self):
        """Return the next element,or else raise StopIteration error."""



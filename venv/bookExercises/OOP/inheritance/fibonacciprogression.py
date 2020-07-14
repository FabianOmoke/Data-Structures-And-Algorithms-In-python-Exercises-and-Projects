from inheritanceProgressionClass import Progression

class FibonacciProgression(Progression):
    """INHERIT FROM PROGRESSION
    iterator producing a generalized Fibonacci progression
    """

    def __init__(self, first=0, second=1):
        """Create a new fibonacci progression
        first = first progression term
        second = second progression term
        """
        super().__init__(first) # start progression at first
        self._prev = second - first # fictitious value preceeding the first

    def _advance(self):
        """Update current value by taking sum of previous two"""
        self._prev, self._current = self._current, self._prev + self._current



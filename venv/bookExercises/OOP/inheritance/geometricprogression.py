from inheritanceProgressionClass import Progression

class GeometricProgression(Progression): #Inherit from Progression
    """Iterator producing a geometric progression"""

    def __init__(self, base=0, start=1):
        """Create a new geometric progression
        base = the fixed constant to multiply each term with
        start = the first term of the progression (default 1)"""

        super().__init__(start)
        self._base = base

    def _advance(self):         #override inherited version
        """Update current value by multiplying it with the base value"""
        self._current *= self._base


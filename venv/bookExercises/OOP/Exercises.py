"""Exercise R-2.4"""

class Flower:
    """A description of  flower"""

    def __init__(self, name, petals=1, price=0):
        self._name = name
        self._petals = petals
        self._price = price

    def set_petals(self,k):
        """Set flower's petal numbers"""
        self._petals = k

    def set_price(self, k):
        """set price of flower"""
        self._price = k

    def set_name(self, name):
        """set price of flower"""
        self._price = name

    def get_name(self):
        """get the name of the flower"""
        return self._name

    def get_petals(self):
        """get the number of petals"""
        return self._petals

    def get_name(self):
        """get the price of the flower"""
        return self._price







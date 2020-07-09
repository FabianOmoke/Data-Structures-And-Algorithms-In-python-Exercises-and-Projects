class CreditCard:
    """create a new instance of a credit card"""
    def __init__(self, customer, bank, acnt, limit):
        """Create a new credit card instance
           initial balance is zero
           customer = name of customer (e.g 'John Wick')
           bank = name of bank (e.g 'OTP')
           acnt = account identifier (e.g '5391 2345 5678 8954')
           limit = credit limit (measuresd in euros)
        """
        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """Return name of customer"""
        return self._customer

    def get_bank(self):
        """Return name of bank"""
        return self._bank

    def get_acnt(self):
        """Return name(number) of account"""
        return self._acnt

    def get_limit(self):
        """Return bank account limit"""
        return self._limit

    def get_balance(self):
        """Return account balance"""
        return self._balance

    def charge(self, price):
        """ Charge given price to the card accordance to current credit limit
        Return True if charge processed, False otherwise
        """
        if price + self._balance > self._limit: #if charge exceeds limit
            return False                        # Charge denied
        else:
            self._balance += price
            return True   #charge accepted

    def make_payment(self,amount):
        """Process customer payment that reduces balance"""
        self._balance -= amount

    

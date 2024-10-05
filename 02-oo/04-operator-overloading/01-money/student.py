class Money:

    def __init__(self,amount,currency):
        self.amount = amount
        self.currency = currency

    @property
    def amount(self):
        return self.__amount
    
    @property
    def currency(self):
        return self.__currency
    
    @amount.setter
    def amount(self,value):
        self.__amount = value

    @currency.setter
    def currency(self,curr):
        self.__currency = curr

    def __add__(self,other):
        if self.currency != other.currency:
            raise RuntimeError("Mismatched currencies!")
        else:
            total_amount = self.amount + other.amount
            return Money(total_amount,self.currency)
        
    def __sub__(self,other):
        if self.currency != other.currency:
            raise RuntimeError("Mismatched currencies!")
        else:
            total_amount = self.amount - other.amount
            return Money(total_amount,self.currency)
    
    def __mul__(self,value):
        return Money(self.amount * value,self.currency)
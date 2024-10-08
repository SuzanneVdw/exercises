class Duration:

    def __init__(self, *, amount_in_seconds):
        self.amount_in_seconds = amount_in_seconds

    @property
    def seconds(self):
        return self.amount_in_seconds
    
    @property
    def minutes(self):
        return self.amount_in_seconds/60
    
    @property
    def hours(self):
        return self.amount_in_seconds/3600

    @staticmethod
    def from_seconds(amount):
        return Duration(amount_in_seconds=amount)
    
    @staticmethod
    def from_minutes(amount):
        return Duration(amount_in_seconds=amount*60)
    
    @staticmethod
    def from_hours(amount):
        return Duration(amount_in_seconds=amount*3600)
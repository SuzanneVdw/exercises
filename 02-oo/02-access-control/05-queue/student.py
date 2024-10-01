class Queue:

    def __init__(self):
        self.items = []

    def add(self,item):
        self.items.append(item)

    def next(self):
        next_in_line = self.items[0]
        self.items.remove(next_in_line)
        return next_in_line
    
    def is_empty(self):
        if self.items == []:
            return True
        return False
class CircularBuffer:

    def __init__(self,max_size):
        self.max_size = max_size
        self.buffer = []

    def __len__(self):
        return len(self.buffer)
    
    def __getitem__(self,index):
        return self.buffer[index]

    def add(self,item):
        self.buffer.append(item)
        if len(self) > self.max_size:
            self.buffer.pop(0)
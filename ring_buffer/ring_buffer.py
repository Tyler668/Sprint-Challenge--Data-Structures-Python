class RingBuffer:
    def  __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.age = 0

    def append(self, value):
        if len(self.storage) < self.capacity:
            self.storage.append(value)
        else:
            self.storage[self.age] = value
            if self.age < self.capacity - 1:
                self.age += 1
            else:
                self.age = 0

    def get(self):
        return self.storage

    
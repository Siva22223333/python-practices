class Counter:
    def __init__(self):
        self.value=0

    def increment(self):
        self.value = self.value + 1

    def reset(self):
        self.value = 0
        print("Reset :",self.value)

obj = Counter()
obj.increment()
obj.increment()
obj.increment()

print("Increment : ",obj.value)

obj.reset()
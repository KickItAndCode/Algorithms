class Deque(object):
    def __init__(self):
        self.items = []

    def Size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def AddToFront(self, item):
        self.items.insert(0, item)

    def AddToBack(self, item):
        self.items.append(item)

    def RemoveFromFront(self):
        return self.items.pop()

    def RemoveFromBack(self):
        return self.items.pop(0)


myDeque = Deque()


myDeque.AddToBack(15)
myDeque.AddToBack(7)
myDeque.AddToFront(5)

print(myDeque.RemoveFromBack())
print(myDeque.RemoveFromBack())
print(myDeque.RemoveFromFront())
print(myDeque.Size())

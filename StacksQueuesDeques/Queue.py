class Queue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def Enqueue(self,item):
        self.items.insert(0,item)

    def Dequeue(self):
        return self.items.pop()

    def Size(self):
        return len(self.items)

q = Queue()
print(q.Size())
print(q.isEmpty())
q.Enqueue(5)
q.Enqueue(10)
q.Enqueue(20)
print (q.Dequeue())

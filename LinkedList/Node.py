class Node (object):
    def __init__ (self, value):
        self.value = value
        self.nextnode = None


    def remove(self, data, previousNode):
        if self.value == data:
            previousNode.nextnode = self.nextnode
            del self.data
            del self.nextnode
        else:
            if self.nextnode is not None:
                self.nextnode.remove(data,self)


a = Node(1)
b = Node(2)
c = Node(3)
a.nextnode = b
b.nextnode = c
print(a.value)
print(a.nextnode.value)
print(b.nextnode.value)

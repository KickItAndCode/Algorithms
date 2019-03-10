from Node import *
from nose.tools import assert_equal

def reverse(head):
    curr = head
    prev = None
    next = None

    while curr:

        next = curr.nextnode
        curr.next = prev
        prev = curr
        curr = next
    return prev




# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.nextnode = b
b.nextnode = c
c.nextnode = d

print (a.nextnode.value)
print (b.nextnode.value)
print (c.nextnode.value)
#
reverse(a)
#
#
print (d.nextnode.value)
print (c.nextnode.value)
print (b.nextnode.value)


#http://www.pythontutor.com/visualize.html#code=class%20Node%20%28object%29%3A%0A%20%20%20%20def%20__init__%20%28self,%20value%29%3A%0A%20%20%20%20%20%20%20%20self.value%20%3D%20value%0A%20%20%20%20%20%20%20%20self.nextnode%20%3D%20None%0A%0Adef%20reverse%28head%29%3A%0A%20%20%20%20curr%20%3D%20head%0A%20%20%20%20prev%20%3D%20None%0A%20%20%20%20next%20%3D%20None%0A%0A%20%20%20%20while%20curr%3A%0A%0A%20%20%20%20%20%20%20%20next%20%3D%20curr.nextnode%0A%20%20%20%20%20%20%20%20curr.next%20%3D%20prev%0A%20%20%20%20%20%20%20%20prev%20%3D%20curr%0A%20%20%20%20%20%20%20%20curr%20%3D%20next%0A%20%20%20%20return%20prev%0A%0A%23%20Create%20a%20list%20of%204%20nodes%0Aa%20%3D%20Node%281%29%0Ab%20%3D%20Node%282%29%0Ac%20%3D%20Node%283%29%0Ad%20%3D%20Node%284%29%0A%0A%23%20Set%20up%20order%20a,b,c,d%20with%20values%201,2,3,4%0Aa.nextnode%20%3D%20b%0Ab.nextnode%20%3D%20c%0Ac.nextnode%20%3D%20d%0A%0Aprint%20%28a.nextnode.value%29%0Aprint%20%28b.nextnode.value%29%0Aprint%20%28c.nextnode.value%29%0A%23%0Areverse%28a%29%0A%23%0A%23%0Aprint%20%28d.nextnode.value%29%0Aprint%20%28c.nextnode.value%29%0Aprint%20%28b.nextnode.value%29&cumulative=false&curInstr=46&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
#

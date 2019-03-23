class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val =  val 


def Height(root):
   
    if root is None:
        return 0

    left  = Height(root.left)
    right = Height(root.right)
    return max(left, right) + 1


root = Node(2)
root.left = Node(1)
root.right = Node(3)

print(Height(root))
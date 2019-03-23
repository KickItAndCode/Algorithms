class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val =  val 


def Size(root):
   
    if root is None:
        return 0

    left =  Size(root.left)
    right =  Size(root.right)

    return left + right + 1


root = Node(2)
root.left = Node(1)
root.right = Node(3)
root.right.right = Node(4)

print(Size(root))
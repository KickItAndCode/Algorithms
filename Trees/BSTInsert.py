class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val =  val 



def insert(root, node):
    if not root:
        return node

    parent, curr = None, root
    while curr is not None:
        parent = curr
        if curr.val <= node.val:
            curr = curr.right
        else:
            curr = curr.left
    
    if parent.val <= node.val:
        parent.right = node
    else:
        parent.left = node
    
    return root

def insertRec(root, node):
   
    
    if root.val < node.val:
        if root.right is None:
            root.right = node
        else:
            insertRec(root.right, node)

    if root.val > node.val:
        if root.left is None:
            root.left = node
        else:
            insertRec(root.left,node)

    return root

def insertIntoBST(self, root: Node, val: int) -> Node:
    
    def helper(root, val):
        if root is None:
            root = Node(val)
        
        if root.val < val:
            if root.right is None:
                root.right = Node(val)
            else:
                self.insertIntoBST(root.right, val)

        if root.val > val:
            if root.left is None:
                root.left = Node(val)
            else:
                self.insertIntoBST(root.left, val)

        
    helper(root, val)
    return root

root = Node(2)
root.left = Node(1)
root.right = Node(3)

insertRec(root, Node(5))
class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val =  val 


"""
using recursion identify find out if the current value
is greater than the max of the two nodes you're trying to find
if so recursively look on the left side 

if the current value is less than the min of the two nodes then 
look on the right

otherwise return the root as that is the LCA

"""
def lca(root, n1, n2):
    
    if root is None:
        return None

    if root.val > max (n1, n2):
        return lca(root.left, n1, n2)
    elif root.val < min (n1, n2):
        return lca(root.right, n1, n2)
    else:
        return root

# Let us construct the BST shown in the figure 
root = Node(20) 
root.left = Node(8) 
root.right = Node(22) 
root.left.left = Node(4) 
root.left.right = Node(12) 
root.left.right.left = Node(10) 
root.left.right.right = Node(14) 
  
n1 = 10 ; n2 = 14
t = lca(root, n1, n2) 
print (f"LCA of {n1} and {n2} is {t.val}")
  
n1 = 14 ; n2 = 8
t = lca(root, n1, n2) 
print (f"LCA of {n1} and {n2} is {t.val}")
  
n1 = 10 ; n2 = 22
t = lca(root, n1, n2) 
print (f"LCA of {n1} and {n2} is {t.val}")
  


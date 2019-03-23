class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val =  val 


"""
Return the path that adds up to the sum specified

Subtract current val from the sum you're looking for
recursively until you get to a leaf
If you get to a leaf and the sum is equal to the current val 
then you 

"""

def RootToLeafSum(root, sum, res):
    if root is None: 
        return False
    
    # LEAF case
    if root.left is None and root.right is None:
        if root.val == sum:
            res.append(root.val)
            return True
        else: return False
        
    if RootToLeafSum(root.left, sum - root.val, res):
        res.append(root.val)
        return True
    if RootToLeafSum(root.right, sum - root.val, res):
        res.append(root.val)
        return True
    
    return False



root = Node(2)
root.left = Node(1)
root.right = Node(3)

print(RootToLeafSum(root, 5, []))
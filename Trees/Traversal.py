# Root -> Left -> Right

def PreOrder (tree):
     if tree:
         print(tree.getRootVal())
         PreOrder(tree.getLeftChild())
         PreOrder(tree.getRightChild())


# Left -> Right -> Root
def PostOrder (tree):
    if tree:
        PostOrder(tree.getLeftChild())
        PostOrder(tree.getRightChild())
        print(tree.getRootVal())

def InOrder(tree):
    if tree:
        InOrder(tree.getLeftChild())
        print(tree.getRootVal())
        InOrder(tree.getRightChild())

    

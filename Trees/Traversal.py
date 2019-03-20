
# Root -> Left -> Right

def PreOrder (tree):
     if tree:
         print(tree.getRootVal())
         PreOrder(tree.getLeftChild())
         PreOrder(tree.getRightChild())


def IterativePreOrder(tree):
    if tree:
        stack = Stack()
        stack.push(tree)

        while stack.isEmpty() == False:
            curr = stack.pop()
            print(curr.getRootVal())
            if curr.rightChild is not None:
                stack.push(curr.rightChild)
            if curr.leftChild is not None:
                stack.push(curr.leftChild)


# Left -> Right -> Root
def PostOrder (tree):
    if tree:
        PostOrder(tree.getLeftChild())
        PostOrder(tree.getRightChild())
        print(tree.getRootVal())

def IterativePostOrder(tree):
    curr = tree
    stack = Stack()
    while curr is not None or  stack.isEmpty() == False:
        if curr:
            stack.push(curr)
            curr = curr.leftChild
        else:
            temp = stack.peek().rightChild
            if temp is None:
                temp = stack.pop()
                print(temp.getRootVal())

                while stack.isEmpty() == False and temp == stack.peek().rightChild:
                    temp = stack.pop()
                    print(temp.getRootVal())
            else:
                curr = temp

#Left -> Root -> Right
def InOrder(tree):
    if tree:
        InOrder(tree.getLeftChild())
        print(tree.getRootVal())
        InOrder(tree.getRightChild())


def IterativeInOrder(tree):
    if tree:
        stack = Stack()
        while True:
            if tree:
                stack.push(tree)
                tree = tree.leftChild
            else:
                if stack.isEmpty():
                    break
                else:
                    tree = stack.pop()
                    print(tree.getRootVal())
                    tree == tree.rightChild

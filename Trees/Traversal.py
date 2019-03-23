from collections import deque

# Root -> Left -> Right

def PreOrder (tree):
     if tree:
         print(tree.getRootVal())
         PreOrder(tree.getLeftChild())
         PreOrder(tree.getRightChild())


def IterativePreOrder(tree):
    if tree:
        stack = deque()
        stack.append(tree)

        while stack.count > 0:
            curr = stack.pop()
            print(curr.getRootVal())
            if curr.rightChild is not None:
                stack.append(curr.rightChild)
            if curr.leftChild is not None:
                stack.append(curr.leftChild)


# Left -> Right -> Root
def PostOrder (tree):
    if tree:
        PostOrder(tree.getLeftChild())
        PostOrder(tree.getRightChild())
        print(tree.getRootVal())

def IterativePostOrder(tree):
    curr = tree
    stack = deque()
    while curr is not None or  stack.count > 0:
        if curr:
            stack.append(curr)
            curr = curr.leftChild
        else:
            temp = stack[-1].rightChild
            if temp is None:
                temp = stack.pop()
                print(temp.getRootVal())

                while stack.count > 0 and temp == stack[-1].rightChild:
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
        stack = deque()
        while True:
            if tree:
                stack.append(tree)
                tree = tree.leftChild
            else:
                if stack.count == 0:
                    break
                else:
                    tree = stack.pop()
                    print(tree.getRootVal())
                    tree == tree.rightChild

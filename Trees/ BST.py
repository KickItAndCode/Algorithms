class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        curr = self
        while True:
            if value < curr.value:
                if curr.left is None:
                    curr.left = BST(value)
                    break
                else:
                    curr = curr.left
            else:
                if curr.right is None:
                    curr.right = BST(value)
                    break
                else:
                    curr = curr.right
        return self

    def contains(self, value):
        curr = self
        while curr is not None:
            if value < curr.value:
                curr = curr.left
            elif value > curr.value:
                curr = curr.right:
            else:
                return True
        return False

    def remove(self, value, parent=None):

       # Search for Node
        curr = self
        while curr is not None:
        if value < curr.value:
            parent = curr
            curr = curr.left
        elif value > curr.value:
            parent = curr
            curr = curr.right
        # Found Note
        else:
            # Two children
            if curr.left is not None:
                and curr.right is not None:
                curr.value = curr.right.getMinValue()
                curr.right.remove(curr.value, curr)
            elif parent == None:
                if curr.left is not None:
                    curr.value = curr.left.value
                    curr.right = curr.left.right
                    curr.left = curr.left.left
                elif curr.right is not None:
                    curr.value = curr.right.value
                    curr.left = curr.right.left
                    curr.right = curr.right.right
                # no children so deleting any reference to the bst
                else:
                    curr.value = None
            elif parent.left == curr:
                parent.left = curr.left if curr.left is not None else curr.right
            elif parent.right == curr:
                parent.right = curr.left if curr.left is not None else curr.right
            break

        return self

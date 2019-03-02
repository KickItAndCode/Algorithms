def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, float("inf"))

def findClosestValueInBstHelper(tree, target, closest):
    if tree is None:
        return closest
    if  abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if tree.value < target:
        return findClosestValueInBstHelper(tree.left, target, closest)
    elif tree.value > target:
        return findClosestValueInBstHelper(tree.right, target, closest)
    else:
        return closest

def findClosestValueInBstHelper(tree, target, closest):
    curr = tree
    while curr is not None:
        if  abs(target - closest) > abs(target - curr.value):
            closest = curr.value
        if curr.value < target:
           curr = curr.left
        elif tree.value > target:
            curr = curr.right
        else:
            break
    return closest  
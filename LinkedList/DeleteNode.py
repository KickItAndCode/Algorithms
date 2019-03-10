def deleteNode(head, valueToDelete):
    currentNode = head
    previousNode = None
    while currentNode is not None:
        if currentNode.value == valueToDelete:
            if previousNode is None:
                newHead = currentNode.nextNode
                currentNode.nextNode = None
                return newHead # Deleted the head
            previousNode.nextNode = currentNode.nextNode
            return head
        previousNode = currentNode
        currentNode = currentNode.nextNode
    return head # Value to delete was not found. 

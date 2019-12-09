# 138. Copy List with Random Pointer
# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

# Return a deep copy of the list.


# Example 1:


# Input:
# {"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

# Explanation:
# Node 1's value is 1, both of its next and random pointer points to Node 2.
# Node 2's value is 2, its next pointer points to null and its random pointer points to itself.


# Note:

# You must return the copy of the given head as a reference to the cloned list.


# In the above diagram, for a given node the next pointer points to the next node in the linked list. The next pointer is something standard for a linked list and this is what links the nodes together. What is interesting about the diagram and this problem is the random pointer which, as the name suggests can point to any node in the linked list or can be a null.

# Approach 1: Recursive
# Intuition

# The basic idea behind the recursive solution is to consider the linked list like a graph. Every node of the Linked List has 2 pointers (edges in a graph). Since, random pointers add the randomness to the structure we might visit the same node again leading to cycles.


# In the diagram above we can see the random pointer points back to the previously seen node hence leading to a cycle. We need to take care of these cycles in the implementation.

# All we do in this approach is to just traverse the graph and clone it. Cloning essentially means creating a new node for every unseen node you encounter. The traversal part will happen recursively in a depth first manner. Note that we have to keep track of nodes already processed because, as pointed out earlier, we can have cycles because of the random pointers.

# Algorithm

# Start traversing the graph from head node.

# Lets see the linked structure as a graph. Below is the graph representation of the above linked list example.


# In the above example head is where we begin our graph traversal.

# If we already have a cloned copy of the current node in the visited dictionary, we use the cloned node reference.

# If we don't have a cloned copy in the visited dictionary, we create a new node and add it to the visited dictionary. visited_dictionary[current_node] = cloned_node_for_current_node.

# We then make two recursive calls, one using the random pointer and the other using next pointer. The diagram from step 1, shows random and next pointers in red and blue color respectively. Essentially we are making recursive calls for the children of the current node. In this implementation, the children are the nodes pointed by the random and the next pointers.

# cloned_node_for_current_node.next = copyRandomList(current_node.next);
# cloned_node_for_current_node.random = copyRandomList(current_node.random);

class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:

    def __init__(self):
        # Dictionary which holds old nodes as keys and new nodes as its values.
        self.visitedHash = {}

    def copyRandomList(self, head):

        if head == None:
            return None

        # If we have already processed the current node, then we simply return the cloned version of it.
        if head in self.visitedHash:
            return self.visitedHash[head]

        # create a new node
        # with the value same as old node.
        node = Node(head.val, None, None)

        # Save this value in the hash map. This is needed since there might be
        # loops during traversal due to randomness of random pointers and this would help us avoid them.
        self.visitedHash[head] = node

        # Recursively copy the remaining linked list starting once from the next pointer and then from the random pointer.
        # Thus we have two independent recursive calls.
        # Finally we update the next and random pointers for the new node created.
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node

#     Complexity Analysis

# Time Complexity: O(N)O(N) where N is the number of nodes in the linked list.
# Space Complexity: O(N)O(N). If we look closely, we have the recursion stack and we also have the space complexity to keep track of nodes already cloned i.e. using the visited dictionary. But asymptotically, the complexity is O(N)O(N).


class Solution:

    def __init__(self):
        # Dictionary which holds old nodes as keys and new nodes as its values.
        self.cloneMap = {}

    def copyRandomList(self, head: 'Node') -> 'Node':
        curr = head

        # first pass put all nodes in the clone mapping
        while curr:
            self.cloneMap[curr] = Node(curr.val, None, None)
            curr = curr.next

        # second pass reset head pointer
        # give all clones their next and random pointer assignments

        curr = head
        while curr:
            self.cloneMap.get(curr).next = self.cloneMap.get(curr.next)
            self.cloneMap.get(curr).random = self.cloneMap.get(curr.random)
            curr = curr.next

        return self.cloneMap.get(head)

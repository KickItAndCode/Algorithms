# 133. Clone Graph

# Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.


# Example:


# Input:
# {"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}

# Explanation:
# Node 1's value is 1, and it has two neighbors: Node 2 and 4.
# Node 2's value is 2, and it has two neighbors: Node 1 and 3.
# Node 3's value is 3, and it has two neighbors: Node 2 and 4.
# Node 4's value is 4, and it has two neighbors: Node 1 and 3.


# Note:

# The number of nodes will be between 1 and 100.
# The undirected graph is a simple graph, which means no repeated edges and no self-loops in the graph.
# Since the graph is undirected, if node p has node q as neighbor, then node q must have node p as neighbor too.
# You must return the copy of the given node as a reference to the cloned graph.


class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        cloneMap = {}
        queue = []

        # add start node to the queue.. Give the start node a clone in the vertex Map
        queue.append(node)
        cloneMap[node] = Node(node.val, [])

        # the BFS continuous until we have processed all vertices in the original graph. Done when queue is empty

        while queue:
            curr = queue.pop(0)

            # loop through connections
            for neighbor in curr.neighbors:

                # if not in our map add it and to the queue
                if neighbor not in cloneMap:
                    cloneMap[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)

                # draw the edge from curr's clone to neighbors clone
                cloneMap[curr].neighbors.append(cloneMap[neighbor])

        # return the clone of the start
        return cloneMap[node]

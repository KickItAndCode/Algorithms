# Find the number connected component in the undirected graph. Each node in the graph contains a label and a list of its neighbors. (a connected component (or just component) of an undirected graph is a subgraph in which any two vertices are connected to each other by paths, and which is connected to no additional vertices in the supergraph.)

# Each connected component should sort by label.


# Example
# Given graph:

# A------B  C
#  \     |  |
#   \    |  |
#    \   |  |
#     \  |  |
#       D   E
# Return {A,B,D}, {C,E}. Since there are two connected component which is {A,B,D}, {C,E}

# Python program to print connected
# components in an undirected graph

# Solution Strategy

# 1) Initialize all vertices as not visited.
# 2) Do following for every vertex 'v'.
#        (a) If 'v' is not visited before, call DFSUtil(v)
#        (b) Print new line character

# DFSUtil(v)
# 1) Mark 'v' as visited.
# 2) Print 'v'
# 3) Do following for every adjacent 'u' of 'v'.
#      If 'u' is not visited, then recursively call DFSUtil(u)
class Graph:

    # init function to declare class variables
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]

    # Time complexity of above solution is O(V + E) as it does simple DFS for given graph.

    def connectedComponents(self):
        visited = []
        cc = []
        for i in range(self.V):
            visited.append(False)
        for v in range(self.V):
            if visited[v] == False:
                temp = []
                cc.append(self.DFSUtil(temp, v, visited))
        return cc

    def DFSUtil(self, temp, v, visited):

        # Mark the current vertex as visited
        visited[v] = True

        # Store the vertex to list
        temp.append(v)

        # Repeat for all vertices adjacent
        # to this vertex v
        for i in self.adj[v]:
            if visited[i] == False:

                # Update the list
                temp = self.DFSUtil(temp, i, visited)
        return temp
    # method to add an undirected edge

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    # Method to retrieve connected components
    # in an undirected graph


# Driver Code
if __name__ == "__main__":

    # Create a graph given in the above diagram
    # 5 vertices numbered from 0 to 4
    g = Graph(5)
    g.addEdge(1, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    cc = g.connectedComponents()
    print("Following are connected components")
    print(cc)

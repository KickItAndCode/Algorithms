class GraphVertex:
    WHITE, GRAY, BLACK = range(3)

    def __init__(self):
        self.color = GraphVertex.WHITE
        self.edges: List['GraphVertex'] = []


def isDeadLocked(graph):
    def hasCycle(curr: GraphVertex):

        # visiting a gray vertex means a cycle
        if curr.color == GraphVertex.GRAY:
            return True

        # visiting curr
        curr.color = GraphVertex.GRAY

        # traverse neighbors
        if any(next.color != GraphVertex.BLACK and hasCycle for next in curr.edges):
            return True

        # mark curr as black
        curr.color = GraphVertex.BLACK
        return False

    return any(vertex.color == GraphVertex.WHITE and hasCycle(vertex) for vertex in graph)


def isDeadLocked(graph):

    def hasCycleDFSUtil(visited: set(GraphVertex), parent: GraphVertex, curr: GraphVertex):
        visited.add(curr)

        for child in curr.edges:
            if child == parent:
                continue

            if child in visited:
                return True

            hasCycle = hasCycleDFSUtil(visited, curr, child)
            if hasCycleDFSUtil:
                return True

        return False

    visited = set()
    for child in graph:
        if child in visited:
            continue

        flag = hasCycleDFSUtil(visited, None, child)
        if flag:
            return True

    return False

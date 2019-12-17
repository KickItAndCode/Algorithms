# 207. Course Schedule
# There are a total of n courses you have to take, labeled from 0 to n-1.

# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

# Example 1:

# Input: 2, [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
#              To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
#              To take course 1 you should have finished course 0, and to take course 0 you should
#              also have finished course 1. So it is impossible.
# Note:

# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.


# this problem can be converted into if a graph contains a cycle
# BFS
def canFinish(numCourses, prerequisites):

    length = len(prerequisites)

    if numCourses == 0 or length == 0:
        return True

    # counter for number of pre reqs
    pCounter = [0] * numCourses
    for i in range(length):
        pCounter[prerequisites[i][0]] += 1

    # store courses that have no pre reqs
    queue = []
    for i in range(numCourses):
        if pCounter[i] == 0:
            queue.append(i)

    numOfCourseWithoutPreReq = len(queue)

    while queue:
        top = queue.pop(0)
        for i in range(length):

            # if a courses pre req can be satified by a course in queue
            if prerequisites[i][1] == top:
                pCounter[prerequisites[i][0]] -= 1

                if pCounter[prerequisites[i][0]] == 0:
                    numOfCourseWithoutPreReq += 1
                    queue.append(prerequisites[i][0])

    return numOfCourseWithoutPreReq == numCourses

# DFS
# better solution


def canFinishDFS(numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    visited = [0 for _ in range(numCourses)]

    # create graph
    for x, y in prerequisites:
        graph[x].append(y)

    # visit each node and do DFS on it
    for i in range(numCourses):
        if not dfs(graph, visited, i):
            return False
    return True


def dfs(graph, visited, i):
    # if ith node is marked as being visited, then a cycle is found
    if visited[i] == -1:
        return False
    # if it is done visted, then do not visit again
    if visited[i] == 1:
        return True
    # mark as being visited
    visited[i] = -1
    # visit all the neighbours
    for j in graph[i]:
        if not dfs(graph, visited, j):
            return False
    # after visit all the neighbours, mark it as done visited
    visited[i] = 1
    return True

# if node v has not been visited, then mark it as 0.
# if node v is being visited, then mark it as -1. If we find a vertex marked as -1 in DFS, then their is a ring.
# if node v has been visited, then mark it as 1. If a vertex was marked as 1, then no ring contains v or its successor


# print(canFinish(1, []))  # true
print(canFinishDFS(2, [[1, 0]]))  # True
print(canFinishDFS(2, [[1, 0], [0, 1]]))  # false

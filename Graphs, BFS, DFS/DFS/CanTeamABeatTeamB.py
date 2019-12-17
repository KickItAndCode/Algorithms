# Given Teams A and B is there a sequence of teams starting witb A and ending with B such that each team in the sequence has beatent he next team in the sequence
from collections import defaultdict, namedtuple
MatchResult = namedtuple(
    "MatchResult", "winningTeam", "losingTeam")

# Time O(E) e for outcomes


def canTeamABeatTeamB(matches, teamA, teamB):
    def buildGraph():
        graph = defaultdict(set)
        for match in matches:
            graph[match.winningTeam].add(match.losingTeam)
        return graph

    def isReachableDFS(graph, curr, dest, visited=set()):
        if curr == dest:
            return True
        elif curr in visited or curr not in graph:
            return False
        visited.add(curr)
        return any(isReachableDFS(graph, team, dest) for team in graph[curr])
    return isReachableDFS(buildGraph(), teamA, teamB)

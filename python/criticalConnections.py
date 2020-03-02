class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        currentRank = 0
        lowestRank = [i for i in range(n)]
        visited = [False for _ in range(n)]
        for connection in connections:
            graph[connection[0]].append(connection[1])
            graph[connection[1]].append(connection[0])
        result = []
        previousVertex = -1
        
        currentVertex = 0
        self._dfs(result, graph, lowestRank, visited, currentRank, previousVertex, currentVertex)
        return result
    
    def _dfs(self, result, graph, lowestRank, visited, currentRank, previousVertex, currentVertex):
        visited[currentVertex] = True
        lowestRank[currentVertex] = currentRank
        
        for nextVertex in graph[currentVertex]:
            if nextVertex == previousVertex:
                continue
            if not visited[nextVertex]:
                self._dfs(result, graph, lowestRank, visited, currentRank + 1, currentVertex, nextVertex)
            lowestRank[currentVertex] = min(lowestRank[currentVertex], lowestRank[nextVertex])
            if lowestRank[nextVertex] >= currentRank + 1:
                result.append([currentVertex, nextVertex])

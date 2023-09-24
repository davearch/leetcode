class Solution:
    def backtrack(self, node: int, path: list[int]) -> None:
        if node == self.target:
            self.res.append(list(path))
            return
        for neighbor in self.graph[node]:
            path.append(neighbor)
            self.backtrack(neighbor, path)
            path.pop()

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.graph, self.res = graph, []
        self.target = len(graph) - 1
        path = [0]
        self.backtrack(0, path)
        return self.res
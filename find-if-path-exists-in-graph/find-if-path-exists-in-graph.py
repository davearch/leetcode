class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = collections.defaultdict(list)
        for src, dest in edges:
            adj_list[src].append(dest)
            adj_list[dest].append(src)
        
        stack, visited = [source], set()
        while stack:
            curr = stack.pop()
            if curr == destination:
                return True
            visited.add(curr)
            for neighbor in adj_list[curr]:
                if neighbor not in visited:
                    stack.append(neighbor)
        return False
            
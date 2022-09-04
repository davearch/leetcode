class Solution:
    def longestPath(self, A: List[int], s: str) -> int:
        n = len(A)
        child_num = [0] * n
        
        # count the number of children for each node
        for a in A[1:]:
            child_num[a] += 1
        
        # The longest valid chain with node i as parent.
        longest = [[0] for _ in range(n)]
        
        # Add all leaf nodes to deque
		# [current node, the maximum length end by this node]
        dq = collections.deque()
        for i in range(n):
            if child_num[i] == 0:
                dq.append([i, 1])
        
        ans = 1
        while dq:
            cur_i, cur_l = dq.popleft()
            cur_p = A[cur_i]
            
            # Minus the number of unvisited child node by 1
            child_num[cur_p] -= 1
            
            # If the child has different char with parent
            if s[cur_p] != s[cur_i]:
                bisect.insort_right(longest[cur_p], cur_l)
                if len(longest[cur_p]) > 2:
                    longest[cur_p].pop(0)
                    
            # If the parent has 0 univisited child, meaning it also
            # become a child node, add it to deque.
            if child_num[cur_p] == 0:
                ans = max(ans, 1 + sum(longest[cur_p][-2:]))
                dq.append([cur_p, 1 + longest[cur_p][-1]])
                
        return ans
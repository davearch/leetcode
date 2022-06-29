class Solution:
    """
    given an integer array `heights` of size n, return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order. A building has an ocean view if all of the buildings to its right has a smaller height.
    
    //maintainability, scalability, readability, and ease to debug before making a decision.
    
    heights = [4,2,3,1]
    [0,2,3]
    
    heights = [4,3,2,1]
    [0,1,2,3]
    
    heights = [1,3,2,4]
    [3]
    
    []
    throw error
    
    [0,0,0]
    [0,1,2]
    
    [1]
    throw error
    
    [-2,-3,2]
    [2]
    
    [-2,-3,-4]
    throw error
    
    [.04,1.3]
    throw error
    
    [1_000_000_000, 10, 1_000_000_001]
    throw error

    """
    def findBuildings(self, heights: List[int]) -> List[int]:
        ans = []
        m = -inf
        for i in range(len(heights) -1, -1, -1):
            if heights[i] > m:
                ans.append(i)
            m = max(m, heights[i])
        return ans[::-1]
        
        
        
        
        
        
        
        
        
        
        
        
        
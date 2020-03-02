'''
Runtime: 36 ms, faster than 99.82% of Python3 online submissions for Rotting Oranges.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Rotting Oranges.
''' 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Possible directions a rot can happen
        dirs = ((0,1), (0,-1), (1,0), (-1,0)) 
        
        # Find row and col length of grid
        row, col = len(grid), len(grid[0])    
        
        # Initialize queue
        queue = []        
        
        # Find rotten oranges
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i,j))
              
        # Initialize time
        t = -1
        
        # While there's new rotten oranges
        while queue:
            
            # Increase time
            t += 1  
            
            # Keep track of new rotten oranges
            new_queue = []
            
            # Go through each rotten orange and rot adjacent oranges
            for i, j in queue:
                for di, dj in dirs:
                    I = i + di
                    J = j + dj
                    if 0 <= I < row and 0 <= J < col and grid[I][J] == 1:
                        grid[I][J] = 2
                        new_queue.append((I,J))
            queue = new_queue
        
        # Check if there are any fresh oranges
        has_fresh = any(
            grid[i][j] == 1 for i in range(row) for j in range(col)
        )
        
        return max(0, t) if not has_fresh else -1

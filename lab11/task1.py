from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Set to track visited cells
        visit = set()

        def dfs(i, j):
            # If out of bounds or at water, contribute 1 to the perimeter
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                return 1
            # If already visited, do not contribute to the perimeter
            if (i, j) in visit:
                return 0

            # Mark the cell as visited
            visit.add((i, j))

            # Sum the perimeter contributions from all directions
            return (
                dfs(i, j + 1) +  # Right
                dfs(i + 1, j) +  # Down
                dfs(i - 1, j) +  # Up
                dfs(i, j - 1)    # Left
            )

        # Find the first land cell and calculate the perimeter
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:  # Start DFS from the first land cell
                    return dfs(i, j)
        
        return 0  # Return 0 if there is no land

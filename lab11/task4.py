from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create an adjacency list for prerequisites
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        
        # Output list to store the course order
        output = []
        # Sets to track visited nodes and nodes in the current path (cycle detection)
        visit, cycle = set(), set()

        def dfs(crs):
            # If the node is in the current path, a cycle exists
            if crs in cycle:
                return False
            # If the node has been visited, it's already processed
            if crs in visit:
                return True
            
            # Mark the node as being visited in the current path
            cycle.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre):  # If a cycle is detected in prerequisites
                    return False
            
            # Remove from the current path and mark as fully visited
            cycle.remove(crs)
            visit.add(crs)
            # Add the course to the output (postorder)
            output.append(crs)
            return True
        
        # Perform DFS for each course
        for c in range(numCourses):
            if not dfs(c):
                return []  # Return empty list if a cycle is detected

        return output[::-1]  # Reverse the output for correct topological order

from typing import List
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # If the initial state is in deadends, it's impossible to proceed
        if "0000" in deadends:
            return -1
        
        # Helper function to generate all possible child states
        def children(lock: str) -> List[str]:
            res = []
            for i in range(4):
                digit = int(lock[i])
                # Turn the wheel forward
                res.append(lock[:i] + str((digit + 1) % 10) + lock[i + 1:])
                # Turn the wheel backward
                res.append(lock[:i] + str((digit - 1 + 10) % 10) + lock[i + 1:])
            return res

        # BFS initialization
        q = deque([("0000", 0)])  # Queue stores (current state, number of turns)
        visited = set(deadends)  # Add deadends to visited to avoid processing them

        while q:
            lock, turns = q.popleft()
            # If we reach the target, return the number of turns
            if lock == target:
                return turns
            # Generate and process all valid child states
            for child in children(lock):
                if child not in visited:
                    visited.add(child)
                    q.append((child, turns + 1))

        # If the queue is exhausted and we haven't reached the target
        return -1

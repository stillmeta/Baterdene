from collections import deque

class MyStack:

    def __init__(self):
        # Initialize an empty deque to simulate stack
        self.q = deque()

    def push(self, x: int) -> None:
        # Add the new element to the queue
        self.q.append(x)
        # Rotate the queue to make the last element the front
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        # Remove and return the front of the queue
        return self.q.popleft()

    def top(self) -> int:
        # Return the front of the queue
        return self.q[0]

    def empty(self) -> bool:
        # Check if the queue is empty
        return not self.q


# Usage Example
# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
print(obj.top())     # Output: 2
print(obj.pop())     # Output: 2
print(obj.empty())   # Output: False

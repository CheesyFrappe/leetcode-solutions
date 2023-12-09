"""
    255 - Implement Stack using Queues - Easy
    https://leetcode.com/problems/implement-stack-using-queues/
    Topics: Stack

    Runtime complexity: Each function runs in O(1) time complexity,
    except push() and pop() functions, those run in O(n) time complexity.
    
    Spacetime complexity: Each function have O(1) space-time complexity

"""

class MyStack:

    def __init__(self):
        self.first_queue = []
        self.second_queue = []

    def push(self, x: int) -> None:
        self.first_queue.append(x)

    def pop(self) -> int:
        while len(self.first_queue) != 1:
            self.second_queue.append(self.first_queue.pop(0))
        res = self.first_queue.pop(0)
        
        while len(self.second_queue) != 0:
            self.first_queue.append(self.second_queue.pop(0))
        return res

    def top(self) -> int:
        return self.first_queue[-1]

    def empty(self) -> bool:
        return len(self.first_queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
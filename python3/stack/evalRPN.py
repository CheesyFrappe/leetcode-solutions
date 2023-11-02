"""
    150 - Evaluate Reverse Polish Notation - Medium
    https://leetcode.com/problems/evaluate-reverse-polish-notation
    Topics: Stack, Array

    Runtime complexity: O(n)
    Spacetime complexity: O(n)
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(v2 - v1)
            elif c == "/":
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(int(v2 / v1))
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(c))
        return stack[0]
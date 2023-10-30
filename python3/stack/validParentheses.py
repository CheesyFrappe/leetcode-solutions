"""
    20 - Valid Parentheses - Easy
    https://leetcode.com/problems/valid-parentheses
    Topics: Stack

    Runtime complexity: O(n)
    Spacetime complexity: O(n)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")":"(","]":"[","}":"{"}
        
        for c in s:
            if c in closeToOpen.keys():
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
        
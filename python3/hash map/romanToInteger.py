"""
    13 - Roman to Integer - Easy
    https://leetcode.com/problems/roman-to-integer/
    Topics: Hash Table, Math

    Time complexity: O(n)
    Space complexity: O(n)
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        prev = 0
        d = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000}
        
        for i in reversed(s):
            curr = d[i]
            if prev > curr:
                total -= curr
            else:
                total += curr
            prev = curr
        return total


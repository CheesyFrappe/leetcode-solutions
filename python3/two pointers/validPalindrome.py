"""
    125 - Valid Palindrome - Easy
    https://leetcode.com/problems/valid-palindrome
    Topics: Two Pointers, String

    Runtime complexity: O(n)
    Spacetime complexity: O(1)
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while not self.check_alpha_num(s[l]) and l < r:
                l += 1
            while not self.check_alpha_num(s[r]) and l < r:
                r -= 1
            if s[l].lower() != s[r].lower():
                print(s[l], s[r])
                return False
            l, r = l + 1, r - 1 
        return True

    def check_alpha_num(self, c):
        return  (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
"""
    3 - Longest Substring Without Repeating Characters - Medium
    https://leetcode.com/problems/longest-substring-without-repeating-characters
    Topics: Sliding Window

    Runtime complexity: O(n)
    Spacetime complexity: O(1)
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        char_set = set()
        res = 0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            res = max(res, r - l + 1)
        return res
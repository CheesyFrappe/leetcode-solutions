"""
    128 - Longest Consecutive Sequence - Medium
    https://leetcode.com/problems/longest-consecutive-sequence
    Topics: Array

    Runtime complexity: O()
    Spacetime complexity: O()
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in nums:
            if (num - 1) not in numSet:
                length = 0
                while (num + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest 

"""
    238 - Product of Array Except Self - Medium
    https://leetcode.com/problems/product-of-array-except-self/
    Topics: Array

    Runtime complexity: O(n)
    Spacetime complexity: O(1)

    Note: find prefix and suffix of each number in nums by iterating the array for each time (O(n));
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
    
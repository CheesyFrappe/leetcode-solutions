"""
    1929 - Concatenation of Array - Easy
    https://leetcode.com/problems/concatenation-of-array/
    Topics: Array

    Runtime complexity: O(1)
    Spacetime complexity: O(n)

    Note: return multiplied array
"""


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        return nums * 2
        
        """
        Second and my first attempt =>

        res = [0] * (2 * len(nums))

        j = 0
        for i in range(len(res)):
            if j == len(nums):
                j = 0
            res[i] = nums[j]
            j += 1
        return res
        """
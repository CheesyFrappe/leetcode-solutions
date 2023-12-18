"""
    1913 - Maximum Product Difference Between Two Pairs - Easy
    https://leetcode.com/problems/maximum-product-difference-between-two-pairs/
    Topics: Array, Sorting

    Runtime complexity: O(n)
    Spacetime complexity: O(n)
"""

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        first_small = second_small = float("inf")
        first_big = second_big = 0

        for n in nums:
            if n < first_small:
                second_small, first_small = first_small, n
            elif n < second_small:
                second_small = n

            if n > first_big:
                second_big, first_big = first_big, n
            elif n > second_big:
                second_big = n
        
        return (first_big * second_big) - (first_small * second_small)

"""
    1475 - Final Prices With a Special Discount in a Shop - Easy
    https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop
    Topics: Stack

    Runtime complexity: O(n)
    Spacetime complexity: O(n)
"""
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []

        for i in range(len(prices)):

            while len(stack) != 0 and prices[stack[-1]] >= prices[i]:
                prices[stack[-1]] -= prices[i]
                stack.pop()
            stack.append(i)
        return prices
        
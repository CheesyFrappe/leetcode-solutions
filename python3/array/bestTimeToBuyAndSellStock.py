"""
    121 - Best Time to Buy and Sell Stock - Easy
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
    Topics: Array

    Runtime complexity = O(n)
    Spacetime complexity = O(1)

    Notes:  use sliding window techinque with two pointers, update slower when faster
            encounter with a slower value than slower's.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        slower = 0
        faster = 1

        while (faster < len(prices)):
            if prices[faster] > prices[slower]:
                if prices[faster] - prices[slower] > max:
                    max = prices[faster] - prices[slower]
            else:
                slower = faster
            faster += 1
        return max
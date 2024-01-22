"""
    645 - Set Mismatch - Easy
    https://leetcode.com/problems/set-mismatch
    Topics: Array, Hash Table

    Runtime complexity: O(n)
    Spacetime complexity: O(n)
"""

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen = set()

        expected_sum = n * (n + 1) // 2
        actual_sum = 0
        duplicate = 0

        for num in nums:
            if num in seen:
                duplicate = num
            seen.add(num)
            actual_sum += num
        
        missing = expected_sum - actual_sum + duplicate
        return [duplicate, missing]
            
            
        

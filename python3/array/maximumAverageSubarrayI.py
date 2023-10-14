"""
    643 - Maximum Average Subarray I - Easy
    https://leetcode.com/problems/maximum-average-subarray-i
    Topics: Array

    Runtime complexity: O(n)
    Spacetime complexity: O(1)

    Note: use sliding window technique
"""
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        j = 0
        count = 0
        max = sum(nums[j:j+k]) / k

        while (j < len(nums)):
            if j - i + 1 < k:
                count += nums[j]
                j += 1
            else:
                count += nums[j]
                if (count / k) > max:
                    max = count / k
                count -= nums[i]
                
                i += 1
                j += 1
        return max
 

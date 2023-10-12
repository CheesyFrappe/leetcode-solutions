"""
    347 - Top K Frequent Elements - Medium
    https://leetcode.com/problems/top-k-frequent-elements/
    Topics: Array, HashMap

    Runtime complexity: O(n)
    Spacetime complexity: O(n)

"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
           count[num] = count.get(num, 0) + 1
        
        for n,c in count.items():
            freq[c].append(n)    

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res 
        
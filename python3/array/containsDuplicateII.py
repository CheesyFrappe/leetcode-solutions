class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict = {}

        for i, n in enumerate(nums):
            if n in dict and abs(i - dict[n]) <= k:
                return True
            else:
                dict[n] = i
        
        return False
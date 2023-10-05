class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for i,j in enumerate(nums):
            if j not in dict:
                dict[j] = i
            else:
                return True
        return False
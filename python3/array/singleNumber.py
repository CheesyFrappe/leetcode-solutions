class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return [x for x in set(nums) if nums.count(x) == 1][0]
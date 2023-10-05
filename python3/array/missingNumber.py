class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 0 1 2 3 5 6

        return sum(range(0, len(nums) + 1)) - sum(nums)


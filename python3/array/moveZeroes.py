class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 0,1,0,3,12 = 0, 1
        # 1,3,0,0,12 = 0, 1
        
        i = 0
        for j in range(len(nums)):
            if nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
            
            if nums[i] != 0:
                i += 1
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        i = 0
        for num in nums:
            res.append(num)
            res.append(nums[n+i])
            i += 1
            if i == n:
                break
        return res

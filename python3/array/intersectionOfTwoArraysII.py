"""
    350 - Intersection of Two Arrays II - Easy
    https://leetcode.com/problems/intersection-of-two-arrays-ii/
    
    Topic: Array

"""
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = Counter(nums1)
        nums2 = Counter(nums2)

        l = []
        for num in nums1:
            if num in nums2:
                min_count = min(nums1[num], nums2[num])
                l += [num] * min_count
        return l
        
        
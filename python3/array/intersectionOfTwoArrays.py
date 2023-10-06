class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = []
        
        for i in set(nums1):
            if i in nums1 and i in nums2:
                l.append(i)
        return l

        """
        one line solution =>
        return set(nums1).intersection(set(nums2))
        """
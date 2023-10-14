"""
    1876 - Substrings of Size Three with Distinct Characters - Easy
    https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters
    Topics: Array

    Runtime complexity: O(n)
    Spacetime complexity: O(1)

    Note: use sliding window technique
"""


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
    
        """
        Long version of same implementation:

        k = 3
        i = 0
        j = 0
        n = len(s)
        count = 0

        while j < n:
            if j - i + 1 < k:
                j += 1
            #elif j - i + 1 == k:
            else:
                if s[i]!=s[i+1] and s[i+1]!=s[i+2] and s[i+2]!=s[i]:
                    count += 1
                j += 1
                i += 1
        return count
        """
        
        count = 0

        for i in range(len(s) - 2):
            if len(set(s[i:i+3])) == 3:
                count+=1
        return count
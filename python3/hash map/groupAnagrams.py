"""
    49 - Group Anagrams - Medium
    https://leetcode.com/problems/group-anagrams
    Topics: String, HashMap

    Runtime complexity: O(n^2)
    Spacetime complexity: O(n)
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list) # mapping charCount to list of anagrams

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1    
            d[tuple(count)].append(s)
        return d.values()
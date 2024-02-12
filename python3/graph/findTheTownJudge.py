"""
    997 - Find the Town Judge - Easy
    https://leetcode.com/problems/find-the-town-judge/
    Topics: Graph

    Time complexity: O(n)
    Space complexity: O(n)
"""

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n == 1:
            return 1

        if not trust and n > 0:
            return -1
        
        d = defaultdict(list)
        judge = -1

        for t in trust:
            d[t[0]].append(t[1])

        for i in range(1, n+1):
            if i not in d.keys():
                judge = i
        
        for u,v in d.items():
            if u != judge and judge not in v:
                return -1

        return judge
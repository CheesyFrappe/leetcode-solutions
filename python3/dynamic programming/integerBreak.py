class Solution:
    def integerBreak(self, n: int) -> int:
        # 12 => 9 => 6 => 3

        if n == 2 or n == 3:
            return n - 1
        
        res = 1
        while (n > 4):
            n -= 3
            res *= 3
        return n * res

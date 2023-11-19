class Solution:
    def climbStairs(self, n: int) -> int:
        f1, f2, ans, i = 1, 1, 0, 2
        if n == 1 or n == 2:
            return n
        else:
            while i <= n:
                ans=f1+f2
                f1=f2
                f2=ans
                i += 1
        return ans

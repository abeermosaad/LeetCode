class Solution:
    def tribonacci(self, n: int) -> int:
        dic = {0 : 0, 1 : 1, 2 : 1}
        for i in range(3,n + 1):
            dic[i] = dic[i - 1] + dic[i - 2] + dic[i - 3]
        return (dic[n])
        
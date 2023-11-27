class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        uniq = 0
        for i in nums:
            uniq ^= i
        return uniq

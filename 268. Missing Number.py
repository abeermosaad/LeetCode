class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        if length not in nums:
            return length
        nums = sorted(nums)
        for i in range(length):
            if i != nums[i]:
                break
        return i

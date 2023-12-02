class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range (len(nums)):
            diff = target - nums[i]
            if diff in dic:
                return[dic[diff], i]
            else:
                dic[nums[i]] = i

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        cur = 0
        for i in range(len(nums)):
            cur += nums[i]
            nums[i] = cur
        return nums
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        k = 0
        while k < len(nums):
            if sum(nums[:k]) == sum(nums[k+1:]):
                return k
            k += 1
        # return (nums[:k],nums[k+1:])
        return -1
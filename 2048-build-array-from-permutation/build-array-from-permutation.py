class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        length = len(nums)
        for i in range(length):
            k = nums[nums[i]]
            nums.append(k)
        #for j in range(length):
          #  nums.pop(j)
            
        return nums[length:]
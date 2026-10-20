class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if nums == []:
            return 0
        uniqe = 1
        for index in range(1,len(nums)):
            last = index-1
            if nums[index] == nums[last]:
                pass
            else:
                nums[uniqe] = nums[index]
                uniqe+=1

        return uniqe
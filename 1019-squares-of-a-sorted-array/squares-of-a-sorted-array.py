class Solution:
    def sortedSquares(self,nums: list[int]) -> list[int]: #! O(2n) Time and O(n) space soultion
        sqr = []
        for index,val in enumerate(nums):
            sqr.append(0)
            nums[index] = val**2
        length = len(nums)-1
        left = 0
        right = length
        while(left <= right):
            if nums[left] < nums[right]:
                sqr[length] = nums[right]
                right -= 1
            elif nums[left] >= nums[right]:
                sqr[length] = nums[left]
                left += 1
            length -= 1
        
        return sqr

        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        if len(nums) == 1:
            return target
             
        for index,value in enumerate(nums):
            if index == 0:
                seen[value] = index
                continue
            temp = target - value
            if temp in seen:
                return(index,seen[temp])
            else:
                seen[value] = index 

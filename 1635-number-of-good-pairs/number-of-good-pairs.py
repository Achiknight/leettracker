class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count = 0
        seen = {}

        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]] = 1                
            else:
                seen[nums[i]] += 1
        
        for j in seen.keys():
            temp = seen[j]
            if temp > 1:
                count += (temp*(temp-1))//2
        return count
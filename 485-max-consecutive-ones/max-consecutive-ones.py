class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        best = 0
        cur = 0
        for i in nums:
            if i == 1:
                cur += 1
            else:
                
                cur = 0
            if cur > best:
                    best = cur
        return best

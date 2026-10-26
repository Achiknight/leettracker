class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        most = 0

        while left < right:
            length = right-left
            cur = min(height[left],height[right])*length
            if cur > most:
                most = cur
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        return most
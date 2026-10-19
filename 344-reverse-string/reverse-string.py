class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        lenght = (len(s)-1)
        for nums in s:
            right = lenght - left
            if left >= right:
                break
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
        
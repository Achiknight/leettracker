class Solution:
    def countDigits(self, num: int) -> int:
        div = 0
        copy = num
        while num > 0:
            dig = num%10
            if copy % dig == 0:
                div += 1
            num = num//10
        return div
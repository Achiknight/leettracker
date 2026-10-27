class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            dig = [int(i) for i in str(num)]
            num = sum(dig)
        return num 

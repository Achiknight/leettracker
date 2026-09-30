class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        elif x == 1:
            return 1
        for i in range(1,x+1):
            if int(x/i) == i:
                return i
            elif int(x/i) == i-1:
                return i-1
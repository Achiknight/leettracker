class Solution:
    def climbStairs(self, n: int) -> int:
        num1 = 0
        num2 = 1
        num3 = 0
        for _ in range(n):
            num3 = num1+num2
            num1 = num2
            num2 = num3
        
        return(num3)
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        Sum = 0
        mult = 1
        while n > 0:
            dig = n%10
            Sum += dig
            mult *= dig
            n = n//10
        return (mult-Sum)
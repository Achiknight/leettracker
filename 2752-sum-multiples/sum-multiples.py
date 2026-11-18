class Solution:
    def sumOfMultiples(self, n: int) -> int:
        def div(k:int) -> int:
            times = n//k
            last = (n//k)*k
            return (times*(k+last))//2
        
        return div(3)+div(5)+div(7)+div(105)-div(3*5)-div(3*7)-div(5*7)
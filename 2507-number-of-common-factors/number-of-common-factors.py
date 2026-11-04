class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        
        if a == 0 or b == 0:
            return 0

        common = 1

        for i in range(2,min(a,b)+1):
            if a%i == 0 and b%i == 0:
                common += 1
        return common
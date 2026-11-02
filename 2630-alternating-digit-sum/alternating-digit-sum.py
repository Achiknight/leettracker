class Solution:
    def alternateDigitSum(self, n: int) -> int:
        itt = 0
        ret = 0
        rev = 0

        while n > 0:
            dig = n%10
            rev = rev*10 + dig
            n = n//10
        
        while rev > 0:
            itt += 1 
            dig = rev%10
            if itt % 2 == 0:
                ret -= dig
            else:
                ret += dig
            rev = rev//10
        return ret
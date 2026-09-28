class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        check = 0
        temp = x
        while x >0:
            dig = x%10
            check = check*10 + dig
            x = x//10
        if temp == check:
            return True
        else:
            return False
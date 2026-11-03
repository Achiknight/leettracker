class Solution:
    def rev(self, num: int) -> int:
        r = 0
        while num > 0:
            dig = num%10
            r = r*10 + dig
            num = num//10
        return r

    def isSameAfterReversals(self, num: int) -> bool:
        rev1 = self.rev(num)
        rev2 = self.rev(rev1)

        if rev2 == num:
            return True
        else:
            return False
        
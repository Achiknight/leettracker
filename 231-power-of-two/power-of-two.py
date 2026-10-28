class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        k = bin(n)[2::]
        if k[0] == "1" and "1" not in k[1::]:
            return True
        return False

class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        big = 0

        tot = 0

        for i in gain:
            tot += i
            if tot > big:
                big = tot
        return big
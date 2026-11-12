class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        bol = []
        top = max(candies)
        cur = 0
        for i in candies:
            cur = extraCandies + i
            if cur >= top:
                bol.append(True)
            else:
                bol.append(False)
        return bol
class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        bol = []
        top = max(candies)
        cur = 0
        for i in range(len(candies)):
            cur = extraCandies + candies[i]
            if cur >= top:
                candies[i] = True
            else:
                candies[i] = False
        return candies
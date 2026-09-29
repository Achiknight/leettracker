class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        if n == 1:
            if needle not in haystack:
                return -1
        k = len(haystack)


        found = False
        for index in range(k):

            if index + n > k:
                return -1
            strip = haystack[index:index+n]
            if needle == strip:
                return index
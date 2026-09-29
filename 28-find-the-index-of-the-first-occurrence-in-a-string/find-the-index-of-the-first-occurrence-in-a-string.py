class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        if n == 1:
            if needle not in haystack:
                return -1
        
        found = False
        for index in range(len(haystack)):

            if index + n > len(haystack):
                return -1
            strip = haystack[index:index+n]
            if needle == strip:
                return index
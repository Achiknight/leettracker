class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        if n == 0:
            return
        arr = (m+n-1)
        m -= 1
        n -= 1
        while arr >=0 :
            
            if n < 0 :
                return
            if m < 0 :

                nums1[arr] = nums2[n]
                n-=1
                arr -=1
                continue
            
            if nums1[m] >= nums2[n]:
                nums1[arr] = nums1[m]
                m -=1
            elif nums1[m] < nums2[n]:
                nums1[arr] = nums2[n]
                n -= 1
            arr -= 1
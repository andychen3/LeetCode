class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        len1 = m - 1
        len2 = n - 1

        for i in range(m + n - 1, -1, -1):
            if len2 < 0:
                break
            if len1 >= 0 and nums1[len1] >= nums2[len2]:
                nums1[i] = nums1[len1]
                len1 -=1
            else:
                nums1[i] = nums2[len2]
                len2 -= 1
        return nums1
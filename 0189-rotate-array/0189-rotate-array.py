class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        ans = [0] * n
        
        for i, num in enumerate(nums):
            ans[(i + k) % n] = num
        nums[:] = ans
        return nums
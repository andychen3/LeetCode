class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        curr = 0

        for index, num in enumerate(nums):
            
            total -= num

            if total == curr:
                return index
            curr += num
        return -1
        

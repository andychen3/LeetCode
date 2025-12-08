class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i = 0
        arr = []

        while n < len(nums):
            arr.append(nums[i])
            arr.append(nums[n])
            i += 1
            n += 1
        
        nums = arr
        
        return nums
        
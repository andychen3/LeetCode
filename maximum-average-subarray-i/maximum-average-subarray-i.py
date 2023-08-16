class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k == 1 and len(nums) == 1:
            return nums[0]
        
        avg = float(-inf)
        left = 0
        total_nums = 0
        running_total = 0
        
        for num in nums:
            running_total += num
            total_nums += 1
            
            while total_nums == k:
                avg = max((running_total)/k, avg)
                running_total -= nums[left]
                left += 1
                total_nums -= 1
        
        return avg
        
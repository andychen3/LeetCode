class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        ans = 0
        distance = float('inf')
        
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                total = nums[i]+nums[j]
                if total < k:
                    new_distance = abs(k-total)
                    if new_distance < distance:
                        distance = new_distance
                        ans = total
                    
        
        
        return ans if ans != 0 else -1
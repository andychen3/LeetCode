class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        N = len(nums)
        ans = []
        nums.sort()
        
        for i in range(N):
            left, right = i+1, N-1
            while left < right:
                total = nums[left] + nums[right]+ nums[i]
                if total == 0 and tuple(sorted((nums[left], nums[right], nums[i]))) not in seen:
                    ans.append([nums[left], nums[right], nums[i]])
                    seen.add(tuple(sorted((nums[left], nums[right], nums[i]))))
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return ans
                    
            
        
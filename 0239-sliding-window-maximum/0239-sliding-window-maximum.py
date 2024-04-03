from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_queue = deque()
        ans = []
        
        for right, num in enumerate(nums):
            while max_queue and nums[max_queue[-1]] <= num:
                max_queue.pop()
            
            max_queue.append(right)
            
            if max_queue[0] + k == right:
                max_queue.popleft()
            
            if right >= k - 1:
                ans.append(nums[max_queue[0]])
        
                
        return ans
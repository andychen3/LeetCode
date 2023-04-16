from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []
        
        for i, num in enumerate(nums):
            while q and nums[q[-1]] < num:
                q.pop()
            q.append(i)
            
            if q[0] + k == i:
                q.popleft()
                
            if i >= k - 1:
                ans.append(nums[q[0]])
        
        return ans
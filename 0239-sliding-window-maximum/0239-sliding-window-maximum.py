from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []
        
        for i in range(len(nums)):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            
            if q[0] + k == i:
                q.popleft()
            
            if i >= k - 1:
                ans.append(nums[q[0]])
        return ans
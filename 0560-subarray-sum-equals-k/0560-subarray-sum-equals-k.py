from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        ans = curr = 0
        counts[0] = 1

        for num in nums:
            curr += num
            # curr - k is current sum - k and i am looking to see if that sum has appeared before 
            ans += counts[curr - k] 
            counts[curr] += 1
        
        return ans
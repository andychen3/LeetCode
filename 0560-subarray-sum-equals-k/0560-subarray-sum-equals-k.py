from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_dict = defaultdict(int)
        sum_dict[0] = 1

        ans = 0
        curr = 0

        for num in nums:
            curr += num
            ans += sum_dict[curr - k]
            sum_dict[curr] += 1
        
        return ans
from collections import defaultdict
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        ans = curr = 0
        
        for i, num in enumerate(nums):
            curr += 1 if num else -1
            if curr == 0:
                ans = max(ans, i + 1)
            elif curr in counts:
                ans = max(ans, i - counts[curr])
            else:
                counts[curr] = i
        return ans
        # hashmap = {}
        # maxlen, count = 0, 0
        # for i in range(len(nums)):
        #     count += 1 if nums[i] == 1 else -1
        #     if count == 0:
        #         maxlen = max(maxlen, i + 1)
        #     elif count in hashmap:
        #         maxlen = max(maxlen, i - hashmap[count])
        #     else:
        #         hashmap[count] = i
        # return maxlen
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
        print(prefix)

        ans = [-1] * len(nums)
        n = (k * 2) + 1
        for i in range(k, len(nums)-k):
            left_bound = prefix[i-k]
            right_bound = prefix[i+k]
            curr = right_bound - left_bound + nums[i - k] # We add back the left most element since it was removed when subtracted from right_bound.
            ans[i] = curr // n
        return ans 

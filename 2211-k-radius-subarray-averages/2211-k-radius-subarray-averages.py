class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
        print(prefix)

        ans = [-1] * len(nums)
        n = (k * 2) + 1
        for i in range(k, len(nums)-k):
            curr = prefix[i + k] - prefix[i - k] + nums[i - k]
            ans[i] = curr // n
        return ans 

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])

        ans = [-1] * len(nums)
        n = (k * 2) + 1
        for i in range(k, len(nums)- k):
            left_bound = prefix[i - k]
            right_bound = prefix[i + k]
            # To get back the leftmost element since we are removing it when we subtract the left bound
            sub_sum = right_bound - left_bound + nums[i-k] 
            ans[i] = sub_sum // n
        return ans
      
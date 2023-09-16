class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ans = [-1] * len(nums)
        n = len(nums)

        # Created prefix sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        # Iterate through the current nums array
        for index in range(k, n - k):
            left_bound = index - k
            right_bound = index + k
            subarray_sum = prefix[right_bound + 1] - prefix[left_bound]
            average = (subarray_sum) // (2 * k + 1)
            ans[index] = average

        return ans
            
            
        
        
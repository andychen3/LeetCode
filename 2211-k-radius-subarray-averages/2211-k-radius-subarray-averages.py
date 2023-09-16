class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = (k * 2) + 1

         # We sum up to k *2 to start our running sum
        running_sum = sum(nums[:2*k])

        ans = [-1] * len(nums)
        # We start at k and then add i + k elements whcih is the next number
        for i in range(k, len(nums)-k):
            running_sum += nums[i + k]
            # We find the average
            ans[i] = running_sum // n
            # Than we remove from the leftmost element
            running_sum -= nums[i-k]
        return ans 
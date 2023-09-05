class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # Many different ways to solve. But we will consider binary search because
        # Subsequence does not matter. We are also given a target from queries
        # We can find the solution space
        nums.sort()

        # build prefix sum since we are trying to find the sum less than queries
        # to make our life easier we can create a prefix
        prefix = [nums[0]]

        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
        
        ans = []

        def binary_search(arr, target):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        for query in queries:
            ans.append(binary_search(prefix, query))
        
        return ans
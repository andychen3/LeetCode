class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        def binary_search(arr, target):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        nums.sort()
        prefix = [nums[0]]
        for num in nums[1:]:
            prefix.append(prefix[-1] + num)
            
        ans = []
        
        for query in queries:
            ans.append(binary_search(prefix, query))
        return ans
            
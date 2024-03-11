class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        def binary_search(arr, target):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
            
            
        nums.sort()
        ans = []
        prefix = [nums[0]]
        for num in nums[1:]:
            prefix.append(prefix[-1] + num)
        
        for query in queries:
            ans.append(binary_search(prefix, query))
        return ans
        
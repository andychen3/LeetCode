class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        def binary_search(arr, target):
            left, right = 0, len(arr) 
            while left < right:
                mid = (left + right) // 2
                if arr[mid] > target:
                    right = mid
                else:
                    left = mid + 1
                    
            return left
            
        nums.sort()
        ans = []
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
        
        for query in queries:
            ans.append(binary_search(prefix, query))
        return ans
        
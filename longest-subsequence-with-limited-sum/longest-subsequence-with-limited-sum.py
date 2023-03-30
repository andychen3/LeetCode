class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # def binary_search(arr, target):
        #     left = 0
        #     right = len(arr)-1
        #     while left <= right:
        #         mid = (left+right) // 2
        #         if arr[mid] == target:
        #             return mid + 1
        #         if arr[mid] > target:
        #             right = mid - 1
        #         else:
        #             left = mid + 1
        #     return left
        
        
        temp = sorted(nums)
        prefix = [temp[0]]
        ans = []
        
        for i in range(len(temp)-1):
            prefix.append(prefix[-1] + temp[i+1])
        
        for num in queries:
            ans.append(bisect.bisect_right(prefix, num))
            
        return ans
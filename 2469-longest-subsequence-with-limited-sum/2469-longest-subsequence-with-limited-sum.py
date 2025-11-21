class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        prefix = [sorted_nums[0]]

        for i in range(1, len(sorted_nums)):
            prefix.append(sorted_nums[i] + prefix[-1])

        def binary_search(query):
            left = 0
            right = len(sorted_nums) - 1
            res = -1

            while left <= right:
                mid = (left + right) // 2

                if prefix[mid] <= query:
                    res = mid
                    left = mid + 1
                else:
                    right = mid - 1
            return res
        
        ans = []

        for q in queries:
            idx = binary_search(q)
            ans.append(idx + 1)
        
        return ans

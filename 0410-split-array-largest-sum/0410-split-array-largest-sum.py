class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(max_sum):
            curr_sum = 0
            splits = 0

            for num in nums:
                if curr_sum + num <= max_sum:
                    curr_sum += num
                else:
                    splits += 1
                    curr_sum = num
            return splits+1 <= k
        left = max(nums)
        right = sum(nums)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        print(right)
        print(mid)
        return left
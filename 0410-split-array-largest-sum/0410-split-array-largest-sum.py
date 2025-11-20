class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(mid):
            groups = 0
            curr = 0

            for num in nums:
                if num > mid:
                    return False

                if curr + num > mid:
                    groups += 1
                    curr = 0
                curr += num
            
            return groups + 1 <= k
        
        left = 0
        right = sum(nums)
        res = 0

        while left <= right:
            mid = (left + right) // 2

            if (check(mid)):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res

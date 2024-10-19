class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        curr = []
        ans = 1
        for num in nums:
            curr.append(num)
            if curr[-1] - curr[0] > k:
                curr = []
                ans += 1
                curr.append(num)
        return ans
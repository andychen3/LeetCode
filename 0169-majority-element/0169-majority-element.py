class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = 0
        freq = 0
        for num in nums:
            if num != ans and freq == 0:
                ans = num
                freq += 1
            elif num == ans:
                freq += 1
            else: 
                freq -= 1
        return ans
        
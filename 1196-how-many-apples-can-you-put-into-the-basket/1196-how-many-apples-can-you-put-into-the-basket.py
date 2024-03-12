class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        ans = 0
        num = 5000
        
        for apple in weight:
            if num - apple >= 0:
                num -= apple
                ans += 1
            else:
                break
        return ans
        
            
class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        res = 0
        basket = 5000
        
        for apple_weight in weight:
            if basket - apple_weight < 0:
                break
            else:
                basket -= apple_weight
                res += 1
        return res
            
        
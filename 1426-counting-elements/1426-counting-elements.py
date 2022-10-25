class Solution:
    def countElements(self, arr: List[int]) -> int:
        res = 0
        
        for num in arr:
            if num+1 in arr:
                res += 1
        return res
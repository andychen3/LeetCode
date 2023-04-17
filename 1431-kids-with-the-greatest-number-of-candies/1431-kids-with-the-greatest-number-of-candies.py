class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        find_max = max(candies)
        res = [0]*len(candies)
        
        for index, candy in enumerate(candies):
            if candy + extraCandies >= find_max:
                res[index] = True
            else:
                res[index] = False
                
        return res
        
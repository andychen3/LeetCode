class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        def check(chunks):
            curr_sweetness = 0
            num_people = 0
            
            for sweets in sweetness:
                curr_sweetness += sweets
                if curr_sweetness >= chunks:
                    curr_sweetness = 0
                    num_people += 1
            
            return num_people < k+1
        
        left = min(sweetness)
        right = sum(sweetness) // (k+1)
        
        while left < right:
            mid = (left + right + 1) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid
        
        return left
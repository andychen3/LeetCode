class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        def check(sweet_level):
            max_sweetness = 0
            num_people = 0
            
            for sweets in sweetness:
                max_sweetness += sweets
                if max_sweetness >= sweet_level:
                    num_people += 1
                    max_sweetness = 0
                    
            return num_people < k + 1
        
        left = min(sweetness)
        right = sum(sweetness) // (k+1)
        
        while left <= right:
            mid = (left+right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
                
        return right
                
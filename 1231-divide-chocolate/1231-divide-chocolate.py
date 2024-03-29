class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        def check(min_sweetness):
            chunks = 0
            num_people = 0
            
            for sweet in sweetness:
                chunks += sweet
                if chunks >= min_sweetness:
                    chunks = 0
                    num_people += 1
            return num_people < k+1
        
        left = min(sweetness)
        right = sum(sweetness) // (k+1)
        
        while left <= right:
            mid = (left+right) //2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
                
        return right
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def binary_search(arr, target):
            left = 0
            right = len(arr) -1
            while left <= right:
                mid = (left+right) // 2
                if arr[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1                    
            return left
                    
        
        ans = []
        potions.sort()
        m = len(potions)
        
        for spell in spells:
            ans.append(m - binary_search(potions, success/spell))
        return ans
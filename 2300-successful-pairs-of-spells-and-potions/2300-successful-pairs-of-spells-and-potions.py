class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def binary_search(multi):
            left, right = 0, len(potions) - 1
            while left <= right:
                mid = (left + right) // 2
                strength = multi * potions[mid]
                if strength < success:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        potions.sort()
        ans = []
        n = len(potions)
        for spell in spells:
            ans.append(n - binary_search(spell))
        return ans
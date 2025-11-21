class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def binary_search(spell):
            left = 0
            right = len(sorted_potions) - 1
            idx = len(sorted_potions)

            while left <= right:
                mid = (left + right) // 2

                if sorted_potions[mid] * spell >= success:
                    idx = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return idx
            
        sorted_potions = sorted(potions)
        res = []
        m = len(sorted_potions)

        for s in spells:
            length = binary_search(s)
            res.append(m - length)
        
        return res
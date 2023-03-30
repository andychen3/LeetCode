class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans = []
        potions.sort()
        m = len(potions)
        
        for spell in spells:
            ans.append(m - bisect.bisect_left(potions, success/spell))
        return ans
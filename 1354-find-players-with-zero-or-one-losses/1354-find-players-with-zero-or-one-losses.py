from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner_set = {winner for winner, _ in matches}
        loser_hash = defaultdict(int)
        
        for _, loser in matches:
            if loser in winner_set:
                winner_set.remove(loser)
            loser_hash[loser] += 1
        
        loser_set = {loser for loser, lost in loser_hash.items() if lost == 1}
        
        
        return [sorted(winner_set), sorted(loser_set)]
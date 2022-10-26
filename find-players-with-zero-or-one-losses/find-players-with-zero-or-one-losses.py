class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        losers = set()
        one_match_losers = collections.defaultdict(int)
        
        for match in matches:
            winners.add(match[0])
            losers.add(match[1])
            one_match_losers[match[1]] += 1
            
        return [sorted(list(winners-losers)), sorted([key for key,value in one_match_losers.items() if value == 1])]
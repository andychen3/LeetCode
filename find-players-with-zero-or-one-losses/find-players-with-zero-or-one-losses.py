from collections import defaultdict

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner_hash = defaultdict(int)
        loser_hash = defaultdict(int)
        winner_list = []
        loser_list = []

        for i in range(len(matches)):
            winners = matches[i][0]
            losers = matches[i][1]
            
            winner_hash[winners] += 1
            loser_hash[losers] += 1
            
        for winners in winner_hash:
            if winners not in loser_hash:
                winner_list.append(winners)
                
        for key, value in loser_hash.items():
            if value == 1:
                loser_list.append(key)
        
        return [sorted(winner_list), sorted(loser_list)]

            
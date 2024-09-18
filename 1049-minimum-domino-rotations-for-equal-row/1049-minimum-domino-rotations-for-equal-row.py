class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)

        top_counts = Counter(tops)
        bot_counts = Counter(bottoms)
        swap_num = None

        for i in range(1, 7):
            if top_counts[i] + bot_counts[i] >= n:
                swap_num = i
                break

        if swap_num == None:
            return -1

        for i in range(n):
            if swap_num not in [tops[i], bottoms[i]]:
                return -1
        
        min_num1 = n - top_counts[swap_num]
        min_num2 = n - bot_counts[swap_num]

        return min(min_num1, min_num2)

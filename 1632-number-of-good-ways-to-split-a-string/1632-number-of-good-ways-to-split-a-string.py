from collections import Counter
class Solution:
    def numSplits(self, s: str) -> int:
        first_split = Counter(s)
        second_split = Counter()
        good_splits = 0

        for char in s:
            first_split[char] -= 1
            if first_split[char] == 0:
                del first_split[char]
            second_split[char] += 1

            if len(first_split) == len(second_split):
                good_splits += 1
        return good_splits
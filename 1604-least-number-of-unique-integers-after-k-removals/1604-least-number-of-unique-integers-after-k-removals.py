from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = Counter(arr)
        freq = sorted(counts.values(), reverse=True) # Sort all the frequency values in reverse order

        while k:
            num = freq[-1] # We want the last element since it is the least frequency
            # If the frequency is enough to decrement k we do it and then pop it
            if num <= k:
                k -= num
                freq.pop()
            else:
                break
        return len(freq)


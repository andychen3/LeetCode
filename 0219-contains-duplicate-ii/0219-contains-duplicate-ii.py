from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        counts = defaultdict(list)

        for idx, num in enumerate(nums):
            counts[num].append(idx)

        for key, val in counts.items():
            if len(val) >= 2:
                for i in range(1, len(val)):
                    if abs(val[i] - val[i-1]) <= k:
                        return True
        return False
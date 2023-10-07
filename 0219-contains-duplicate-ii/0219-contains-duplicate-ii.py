class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = {}

        for idx, num in enumerate(nums):
            if num in hash_map:
                if idx - hash_map[num] <= k:
                    return True
            hash_map[num] = idx
        return False
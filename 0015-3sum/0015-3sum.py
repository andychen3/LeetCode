class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        seen = set()
        ans = []
        
        for i, num in enumerate(nums):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            hash_map = {}
            for j in range(i + 1, len(nums)):
                diff = (num + nums[j]) * -1
                if diff in hash_map:
                    triplets = tuple(sorted([num, nums[j], diff]))
                    if triplets not in seen:
                        seen.add(triplets)
                        ans.append(list(triplets))
                hash_map[nums[j]] = nums[j]
        return ans
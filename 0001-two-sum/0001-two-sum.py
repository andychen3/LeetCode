class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = defaultdict(int)
        
        for index, num in enumerate(nums):
            difference = target-num
            if difference in hash_map:
                return [index, hash_map[difference]]
            else:
                hash_map[num] = index
                
        return -1
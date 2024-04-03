from collections import defaultdict
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_map = defaultdict(int)
        stack = []
        
        for num in nums2:
            while stack and stack[-1] < num:
                hash_map[stack.pop()] = num
            stack.append(num)
        
        return [hash_map[num] if hash_map[num] != 0 else -1 for num in nums1]
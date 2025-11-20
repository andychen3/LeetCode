class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_map = {}
        stack = []

        for num in nums2:
            while stack and num > stack[-1]:
                hash_map[stack.pop()] = num
            stack.append(num)
        
        return [hash_map.get(num, -1) for num in nums1]
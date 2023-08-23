class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        map = {}

        for num in nums2:
            while stack and stack[-1] < num:
                map[stack.pop()] = num
            stack.append(num)
        
        return [map.get(nums, -1) for nums in nums1]



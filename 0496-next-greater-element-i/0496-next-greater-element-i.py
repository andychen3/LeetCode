class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []
        
        for nums in nums2:
            while stack and stack[-1] < nums:
                prev_num = stack.pop()
                next_greater[prev_num] = nums
            stack.append(nums)
        
        return [next_greater.get(num, -1) for num in nums1]
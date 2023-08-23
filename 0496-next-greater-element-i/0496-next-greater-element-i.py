class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        map = {}

        # build the hashmap with numbers:greater number
        for num in nums2:
            while stack and stack[-1] < num:
                map[stack.pop()] = num
            stack.append(num)

        # check if stack is empty
        for num in stack:
            map[num] = -1
        
        return [map[nums] for nums in nums1]


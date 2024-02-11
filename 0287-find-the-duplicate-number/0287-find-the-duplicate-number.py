class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        curr = 0
        
        while True:
            slow = nums[slow]
            curr = nums[curr]
            if slow == curr:
                return slow
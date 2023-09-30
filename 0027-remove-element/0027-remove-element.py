class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ptr = len(nums)-1
        n = len(nums)

        for i in range(n-1, -1, -1):
            if nums[i] == val:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr -= 1
        return ptr+1
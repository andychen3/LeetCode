class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        flag = None
        if nums[0] >= nums[-1]:
            flag = "decreasing"
        else:
            flag = "increasing"
        
        n = len(nums)
        if flag == "increasing":
            for i in range(1, n):
                if nums[i] < nums[i-1]:
                    return False
        else:
            for i in range(1, n):
                if nums[i] > nums[i-1]:
                    return False
        return True
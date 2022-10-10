class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        actual_rotation = k % len(nums)
        
        start = 0
        break_point = (len(nums)-1)-actual_rotation
        end = len(nums)-1
        end_break_point = len(nums)-actual_rotation
        
        def reverse(s,e):
            while s<e:
                nums[s], nums[e] = nums[e], nums[s]
                s +=1
                e -=1
        
        # Reverse the beginning to the break_point
        reverse(start,break_point)
        
        # Reverse the end_break_point to the end
        reverse(end_break_point, end)
        
        # Reverse the whole list
        
        reverse(start,end)
        
        return nums
        
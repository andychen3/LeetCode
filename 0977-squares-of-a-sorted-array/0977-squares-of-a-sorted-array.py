class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        
        left, right = 0, len(nums)-1
        tracker = len(nums)-1
        
        while left <= right:
            left_num = nums[left]**2
            right_num = nums[right]**2
            
            if left_num >= right_num:
                res[tracker] = left_num
                left += 1
            else:
                res[tracker] = right_num
                right -= 1
            tracker -= 1
                
        return res
    
#     # nums = [-4,-1,0,3,10]
#     # [0,1,9,16,100]
    
#     # nums = [-4,-1,0,3,10]
#                   x x
#         left_num = 0
#         right_num = 0
    
#     res = [0,1,9,25,100]
#     left = 3
#     right = 2
#     tracker = 0
    
    
        
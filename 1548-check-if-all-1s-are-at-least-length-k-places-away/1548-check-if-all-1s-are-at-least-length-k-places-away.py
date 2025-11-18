class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        initial_index = -1

        for index, num in enumerate(nums):
            if num == 1 and initial_index == -1:
                initial_index = index
            elif num == 1:
                if index - initial_index - 1 < k:
                    return False
                initial_index = index
        
        return True 

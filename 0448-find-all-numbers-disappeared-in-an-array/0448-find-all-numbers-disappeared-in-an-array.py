class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)):
            while nums[i]!=i+1:
                next_index = nums[i]-1
                if nums[next_index]==nums[i]: # we put this since we do not want to get stuck in a cycle. 
                    break
                nums[i], nums[next_index] = nums[next_index], nums[i]

        ans = []
        for i in range(len(nums)):
            if nums[i]!=i+1:
                ans.append(i+1)
        return ans

        
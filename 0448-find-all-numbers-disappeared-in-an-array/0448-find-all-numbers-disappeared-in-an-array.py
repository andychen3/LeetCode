class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hash_set = set(nums)
        ans = []

        for i in range(1,len(nums)+1):
            if i not in hash_set:
                ans.append(i)
        return ans

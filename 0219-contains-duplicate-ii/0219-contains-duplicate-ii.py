class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Find a duplicate and if there is a duplicate the absolute value of the difference of their indexes
        is less than k.
        
        Param: array of size n
        Param: k = an integer
        
        Return Boolean 
        """
        hash = collections.defaultdict(int)
        
        for index, num in enumerate(nums):
            if num in hash and index - hash[num] <= k:
                return True
            else:
                hash[num] = index
        
        return False

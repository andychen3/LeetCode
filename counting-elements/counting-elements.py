class Solution:
    def countElements(self, arr: List[int]) -> int:
        hash_set = set(arr)
        output = 0
        
        for nums in arr:
            if nums+1 in hash_set:
                output += 1
                
        return output
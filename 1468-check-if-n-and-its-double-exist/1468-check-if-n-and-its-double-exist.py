class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hash_map = {val:key for key, val in enumerate(arr)}
        
        for idx, num in enumerate(arr):
            if num*2 in arr and idx != hash_map[num*2]:
                return True
        return False
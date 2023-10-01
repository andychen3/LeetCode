class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hash_map = {num:idx for idx, num in enumerate(arr)}
        
        for idx, num in enumerate(arr):
            if num*2 in hash_map and idx != hash_map[num*2]:
                return True
            
        return False
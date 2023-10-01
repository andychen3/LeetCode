class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_val = 0
        n = len(arr)
        
        for i in range(n-1,-1,-1):
            temp = arr[i]
            if i == n-1:
                arr[i] = -1
            else:
                arr[i] = max_val
            max_val = max(max_val, temp)
        return arr
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        peak_idx = 0
        n = len(arr)
        
        while peak_idx+1 < n and arr[peak_idx] < arr[peak_idx+1]:
            peak_idx += 1
        
        if peak_idx == 0 or peak_idx == n-1:
            return False
        
        while peak_idx+1 < n and arr[peak_idx] > arr[peak_idx+1]:
            peak_idx += 1
        
        return peak_idx == n-1
        
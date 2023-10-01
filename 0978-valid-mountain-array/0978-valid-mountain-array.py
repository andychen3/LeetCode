class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        # find the peak
        peak = 0
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                peak = i - 1
                break
            if arr[i] == arr[i-1]:
                return False
        
        if peak == 0 or peak == len(arr) - 1:
            return False
        
        for i in range(peak, len(arr)-1):
            if arr[i] <= arr[i+1]:
                return False
        return True

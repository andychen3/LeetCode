class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        peak = 0

        n = len(arr)
        for i in range(n-1):
            if arr[i] >= arr[i+1]:
                peak = i
                break

        if peak == 0 or peak == n - 1:
            return False
        
        while peak+1 < n:
            if arr[peak] <= arr[peak+1]:
                return False
            peak += 1
        return True
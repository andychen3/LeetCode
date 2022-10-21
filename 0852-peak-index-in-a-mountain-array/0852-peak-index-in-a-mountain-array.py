class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        lo = 0
        hi = len(arr)-1
        
        while lo < hi:
            mid = (lo + hi) //2
            
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid] < arr[mid+1]:
                lo = mid
            else:
                hi = mid
        
        
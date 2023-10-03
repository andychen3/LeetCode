class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeros = arr.count(0)
        n = len(arr)

        for i in range(n-1,-1,-1):
            if i + zeros < n:
                arr[i+zeros] = arr[i]
            if arr[i] == 0:
                zeros -= 1
                # We do this second if statement because we are making space for the zeros before it
                # Since the place where we found this element could not be a zero but is suppose to be a zero
                if i + zeros < n:
                    arr[i+zeros] = 0
        return arr
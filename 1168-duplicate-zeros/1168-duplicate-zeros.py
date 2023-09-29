class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeros = arr.count(0)
        n = len(arr)

        for i in range(n-1, -1, -1):
            # If reg element and within bound moves it to the end
            if i + zeros < n:
                arr[i + zeros] = arr[i]
            # If element is zero duplicate it
            if arr[i] == 0:
                zeros -= 1
                if i + zeros < n:
                    arr[i + zeros] = 0
        return arr
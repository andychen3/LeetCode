class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeros = arr.count(0)
        n = len(arr)

        # We do i + zeros because that is where the last element should go to make space for the
        # duplicated zero
        # if we encounter a zero we duplicate it.
        for i in range(n - 1, -1, -1):
            # We do this if statement first to make sure we copy the val if its not 0 somewhere else
            # before we overwrite it with the next if statement.
            if i + zeros < n:
                arr[i + zeros] = arr[i]
            if arr[i] == 0:
                zeros -= 1
                if i + zeros < n:
                    arr[i + zeros] = 0
        return arr
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def backtrack(arr):
            if len(arr) == n:
                # Convert the integers in the arr to a string
                string = [str(i) for i in arr]
                # Join them into one number then add it to the answer
                ans.append(int("".join(string)))
                return
            
            for i in range(10):
                # Avoids adding 0 to the beginning of a number
                # example 08 will be skipped
                if len(arr) == 0 and i == 0:
                    continue
                
                # If the array is originally empty add the first number
                # Else after that you have to check if the next number is at least k apart from
                # the previous integer
                # We use absolute and subtracting so we can simulate the + and -
                if len(arr) == 0 or abs(arr[-1] - i) == k:
                    arr.append(i)
                    backtrack(arr)
                    arr.pop()

        ans = []
        backtrack([])
        return ans
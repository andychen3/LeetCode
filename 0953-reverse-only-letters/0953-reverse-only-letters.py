class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        arr = list(s)
        left, right = 0, len(arr)-1

        while left < right:
            if arr[left].isalpha() and arr[right].isalpha():
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
            elif not arr[left].isalpha():
                left += 1
            elif not arr[right].isalpha():
                right -= 1
        return "".join(arr)
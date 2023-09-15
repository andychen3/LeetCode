class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        left = 0
        right = word.find(ch)
        arr = list(word)

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        
        return "".join(arr)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # what are the base cases?
        #when the string is empty what do you do?
        # What is the recurrence relationship?
        def reverse(word, left, right):
            if left >= right:
                return word
            word[left], word[right] = word[right], word[left]
            return reverse(word, left + 1, right - 1)

        return reverse(s, 0, len(s)-1)
        
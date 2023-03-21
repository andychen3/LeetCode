class Solution:
    def reverseWords(self, s: str) -> str:
        array = s.split(" ")
        
        for index, words in enumerate(array):
            array[index] = self.reverse(words)
        
        return " ".join(array)
        
    def reverse(self, string):
        new_array = list(string)
        
        left = 0
        right = len(new_array)-1
        
        while left < right:
            new_array[left], new_array[right] = new_array[right], new_array[left]
            left += 1
            right -= 1
            
        return "".join(new_array)
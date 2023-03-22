class Solution:
    def reversePrefix(self, word: str, ch: str) -> str: 
        
        def reverse_word(first_index, last_index):
            new_array = list(word)
            while first_index < last_index:
                new_array[first_index], new_array[last_index] = new_array[last_index], new_array[first_index]
                first_index += 1
                last_index -= 1
                
            return "".join(new_array)
        
        for index, char in enumerate(word):
            if char == ch:
                return reverse_word(0, index)
                
        return word
                
                
        
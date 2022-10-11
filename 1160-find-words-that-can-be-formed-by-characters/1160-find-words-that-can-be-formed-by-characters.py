class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        chars_hash = collections.Counter(chars)
        
        for word in words:
            word_hash = collections.Counter(word)
            if all(word_hash[c] <= chars_hash[c] for c in word_hash):
                res += len(word)
    
        return res


                    
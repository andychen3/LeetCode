class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapping = {char: i for i, char in enumerate(order)}
        
        for i in range(1, len(words)):
            w1 = words[i-1]
            w2 = words[i]
            for j in range(len(w1)):
                if j == len(w2):
                    return False
                
                if w1[j] != w2[j]:
                    if mapping[w1[j]] > mapping[w2[j]]:
                        return False
                    break
        return True
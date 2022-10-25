class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        new_set = set(sentence)
        return len(new_set) == 26
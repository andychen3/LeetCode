class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        output = 0
        
        for string in zip(*strs):
            if tuple(sorted(string)) != string:
                output += 1
        return output
                
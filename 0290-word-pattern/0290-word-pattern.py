class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_hash = defaultdict(int)
        pattern_set = set()
        array = s.split()
        if len(pattern) != len(array):
            return False
        
        for index, word in enumerate(array):
            word_pattern = pattern[index]
            if word not in pattern_hash and word_pattern not in pattern_set:
                pattern_hash[word] = word_pattern
                pattern_set.add(word_pattern)
        
        print(pattern_hash)
        for i, patterns in enumerate(pattern):
            word = array[i]
            if pattern_hash[word] != patterns:
                return False
            
        return True
        
        


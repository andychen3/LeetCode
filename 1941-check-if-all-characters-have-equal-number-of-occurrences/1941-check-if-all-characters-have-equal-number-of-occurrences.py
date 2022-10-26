class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counter = collections.Counter(s)
        counter_set = set(counter.values())
        
        return len(counter_set)==1
        
        
        
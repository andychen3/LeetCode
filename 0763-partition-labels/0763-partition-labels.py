class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash_map = {}
        
        for idx, char in enumerate(s):
            hash_map[char] = idx
            
        curr_len = 0
        end = 0
        res = []
        
        for i, char in enumerate(s):
            curr_len += 1
            end = max(end, hash_map[char])
            
            if i == end:
                res.append(curr_len)
                curr_len = 0
        return res
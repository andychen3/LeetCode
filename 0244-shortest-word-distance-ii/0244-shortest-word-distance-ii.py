class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordsDict = wordsDict
        self.wordHash = defaultdict(list)
        
        for index, key in enumerate(self.wordsDict):
            self.wordHash[key].append(index)
            

    def shortest(self, word1: str, word2: str) -> int:
        min_val = float('inf')
        
        index1 = self.wordHash[word1]
        index2 = self.wordHash[word2]
        
        ptr1 = ptr2 = 0
        
        while ptr1 < len(index1) and ptr2 < len(index2):
            min_val = min(min_val, abs(index1[ptr1]-index2[ptr2]))
            if index2[ptr2]> index1[ptr1]:
                ptr1 += 1
            else:
                ptr2 += 1

        # for index1 in self.wordHash[word1]:
        #     for index2 in self.wordHash[word2]:
        #         min_val = min(min_val, abs(index1-index2))
        return min_val

        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
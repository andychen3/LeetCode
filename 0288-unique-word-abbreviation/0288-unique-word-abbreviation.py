from collections import defaultdict
class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.list = dictionary
        self.hash_map = defaultdict(set)

        for words in self.list:
            self.hash_map[self.convert_word(words)].add(words)

    def convert_word(self, word):
        converted = word
        if len(word) > 2:
            converted = word[0] + str(len(word)-2) + word[-1]
        return converted
        

    def isUnique(self, word: str) -> bool:
        converted = self.convert_word(word)
        if converted in self.hash_map and len(self.hash_map[converted]) == 1 and word in self.hash_map[converted]:
            return True
        elif converted not in self.hash_map:
            return True
        else:
            return False
        

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
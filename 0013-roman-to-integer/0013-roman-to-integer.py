class Solution:
    def romanToInt(self, s: str) -> int:
        hash_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':1000}
        output = 0
        special = False

        for index, char in enumerate(s):
            if special:
                special = False
                continue

            if char == 'I' and index + 1 < len(s):
                if s[index+1] == 'V':
                    output += 4
                elif s[index+1] == 'X':
                    output += 9
                else:
                    output += hash_map[char]
                    continue
                special = True
                continue
            elif char == 'X' and index + 1 < len(s):
                if s[index+1] == 'L':
                    output += 40
                elif s[index+1] == 'C':
                    output += 90
                else:
                    output += hash_map[char]
                    continue
                special = True
                continue
            elif char == 'C' and index + 1 < len(s):
                if s[index+1] == 'D':
                    output += 400
                elif s[index+1] == 'M':
                    output += 900
                else:
                    output += hash_map[char]
                    continue
                special = True
                continue
            else:
                output += hash_map[char]
        return output

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return "".join(f"{len(word)}|{word}" for word in strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        ans = []
        i = 0
        while i < len(s):
            idx = s.find("|", i)
            i = idx + 1 + int(s[i: idx])
            ans.append(s[idx+1: i])
        return ans


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        char_counts = Counter()

        for char in s:
            if char == "-":
                continue
            else:
                char_counts[char] += 1
        

        n = sum(char_counts.values())
        if n == 0:
            return ""
        remainder = n % k
        ans = []
        group_count = 0

        for char in s.upper():
            if char == "-":
                continue
            if remainder > 0:
                ans.append(char)
                remainder -= 1
                if remainder == 0:
                    ans.append("-")
                continue
            if group_count < k:
                ans.append(char)
                group_count += 1
                if group_count == k:
                    ans.append("-")
                    group_count = 0
        if ans[-1] == "-":
            ans.pop()
        return "".join(ans)
            


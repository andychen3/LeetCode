class Solution:
    def maximumTime(self, time: str) -> str:
        ans = []
        for i, char in enumerate(time):
            if i == 0 and char == "?":
                if time[i + 1] in "456789":
                    ans.append("1")
                else:
                    ans.append("2")
            elif i == 1 and char == "?":
                if ans[i-1] == "2":
                    ans.append("3")
                else:
                    ans.append("9")
            elif i == 3 and char == "?":
                ans.append("5")
            elif i == 4 and char == "?":
                ans.append("9")
            else:
                ans.append(char)
            
        return "".join(ans)
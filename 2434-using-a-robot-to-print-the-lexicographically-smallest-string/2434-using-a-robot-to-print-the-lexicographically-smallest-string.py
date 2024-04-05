class Solution:
    def robotWithString(self, s: str) -> str:
        ans = []
        increasing = deque()
        stack = []
        
        for letter in s:
            while increasing and increasing[-1] > letter:
                increasing.pop()
            increasing.append(letter)
            
        
        for letter in s:
            if letter == increasing[0]:
                increasing.popleft()
                ans.append(letter)
                while stack and increasing and stack[-1] <= increasing[0]:
                    ans.append(stack.pop())
            else:
                stack.append(letter)
                
        while stack:
            ans.append(stack.pop())
            
        return "".join(ans)
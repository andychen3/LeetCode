class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"
        
        n, m = len(num1), len(num2)
        res = [0] *(n+m)
        num1, num2 = num1[::-1], num2[::-1]
        
        for i in range(n):
            for j in range(m):
                digit = int(num1[i]) * int(num2[j])
                res[i + j] += digit
                res[i + j + 1] += res[i + j] // 10
                res[i + j] = res[i + j] % 10
        
        res, idx = res[::-1], 0
        while idx < len(res) and res[idx] == 0:
            idx += 1
            
        return "".join([str(num) for num in res[idx:]])
        
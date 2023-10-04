class Solution:
    def isHappy(self, n: int) -> bool:
        
        def find_n(n):
            total = 0
            while n:
                n, digits = divmod(n, 10)
                total += digits **2
            return total


        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = find_n(n)
        
        return n == 1
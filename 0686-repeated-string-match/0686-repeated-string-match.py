class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if set(b) - set(a):
            return -1

        min_repeats = (len(b) - 1) // len(a) + 1
        repeated_a = a * min_repeats

        if b in repeated_a:
            return min_repeats
        elif b in repeated_a + a:
            return min_repeats + 1

        return -1

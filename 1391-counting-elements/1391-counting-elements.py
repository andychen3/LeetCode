class Solution:
    def countElements(self, arr: List[int]) -> int:
        hash_set = set(arr)
        res = 0

        for num in arr:
            if num + 1 in hash_set:
                res += 1
        return res

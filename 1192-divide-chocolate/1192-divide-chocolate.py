class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:

        def check(max_sweetness):
            groups = 0
            chunks = 0

            for s in sweetness:
                chunks += s
                if chunks >= mid:
                    groups += 1
                    chunks = 0
            
            return groups >= k + 1

        left, right = 1, sum(sweetness)
        res = 0

        while left <= right:
            mid = (left + right) // 2

            if check(mid):
                res = mid
                left = mid + 1
            else:
                right = mid - 1

        return res
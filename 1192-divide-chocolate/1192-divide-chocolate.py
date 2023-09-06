class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        # The difference between a heap problem and a binary search problem
        # If there is k is what is the k asking?
        # This k is asking for if divided among the k people what is the min total sweetness you get
        # So there is a threshold. While the other problems are asking kth element or kth operations.
        # We also know this is a greedy problem because of min and max.
        def check(sweetness_level):
            ans = 0
            groups = 0

            for sweet in sweetness:
                groups += sweet
                if groups >= sweetness_level:
                    ans += 1
                    groups = 0
            # When do you reduce the sweetness level?
            # When ans is greater than the amount of groups. Which tells us that
            # The sweetness level is not big enough so we have to increase our left range
            return ans >= k + 1 

        # This is the binary search template for finding a maximum
        left = 1
        right = sum(sweetness)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right
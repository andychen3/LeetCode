class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # The reason why we pass a start variable is because we can reuse the same element multiple times
        def backtrack(start, curr_sum, arr):
            if curr_sum == target:
                ans.append(arr[:])
                return
        
            for index in range(start, len(candidates)):
                # We have this check here because we don't want to add any elements if we already
                # know it will get greater than target
                if curr_sum + candidates[index] <= target:
                    arr.append(candidates[index])
                    # The reason why we don't increment index is because we want to reuse the same element
                    # The only thing that moves our recursion is increasing curr_sum
                    backtrack(index, curr_sum + candidates[index], arr)
                    arr.pop()

        ans = []
        backtrack(0, 0, [])
        return ans
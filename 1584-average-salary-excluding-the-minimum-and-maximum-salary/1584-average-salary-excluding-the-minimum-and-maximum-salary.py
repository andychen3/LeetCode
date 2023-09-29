class Solution:
    def average(self, salary: List[int]) -> float:
        min_val = min(salary)
        max_val = max(salary)

        return (sum(salary) - min_val - max_val) / (len(salary) - 2)
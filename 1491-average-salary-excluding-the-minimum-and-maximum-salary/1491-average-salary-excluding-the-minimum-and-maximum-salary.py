class Solution:
    def average(self, salary: List[int]) -> float:
        min_salary = min(salary)
        max_salary = max(salary)
        total = sum(salary)
        res = (total - (min_salary+max_salary)) / (len(salary)-2)
        return res
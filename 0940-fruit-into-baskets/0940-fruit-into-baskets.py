from collections import Counter
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = Counter()
        left = ans = 0

        for right, num in enumerate(fruits):
            basket[num] += 1

            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1
            ans = max(ans, right - left + 1)
        return ans
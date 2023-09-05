class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # How do i know to use binary search? Maybe its the at least key word?
        # Saying that if i was to sort input then all the ones after will be greater than successful
        potions.sort()
        ans = []
        n = len(potions)

        # This keeps the basic BS format
        def binary_search(arr, target):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                # We combine the equal and don't return early if we found mid equal target
                # because if we have duplicates in the array we want to find the index where 
                # the element just became successful
                # This will be in the left most index
                if arr[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return n - left

        for spell in spells:
            ans.append(binary_search(potions, success / spell))

        return ans

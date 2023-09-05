class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # How do i know to use binary search? Maybe its the at least key word?
        # Saying that if i was to sort input then all the ones after will be greater than successful
        potions.sort()
        ans = []
        n = len(potions)

        # This is the binary search pattern to find left most insert point for arrays that contain duplicates
        def binary_search(arr, target):
            left, right = 0, len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            return n - left

        for spell in spells:
            ans.append(binary_search(potions, success / spell))

        return ans

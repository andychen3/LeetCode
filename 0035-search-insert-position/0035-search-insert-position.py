class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # This binary search and left returns the position because left will always stop shy of
        # where the value would be inserted
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # We always do if because this is technically the beginning of the conditions
            # The earlier if is to exit early if target is found
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left
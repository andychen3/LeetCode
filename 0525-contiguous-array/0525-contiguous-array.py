class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashmap = {}
        maxlen, count = 0, 0
        for i in range(len(nums)):
            count += 1 if nums[i] == 1 else -1
            if count == 0:
                maxlen = max(maxlen, i + 1)
            elif count in hashmap:
                maxlen = max(maxlen, i - hashmap[count])
            else:
                hashmap[count] = i
        return maxlen
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        convert = int("".join([str(num)for num in digits]))
        convert += 1

        return [int(num) for num in str(convert)]
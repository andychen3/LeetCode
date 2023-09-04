class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # How do i know this is a greedy problem?
        # It says infinite number of boats which means order doesnt matter
        # We also wnat the min. number of boats to carry so we want to be greedy with filling up the
        # the two boats with the heaviest people that are within the limit
        ans = 0
        people.sort()
        left, right = 0, len(people) - 1

        while left <= right:
            heaviest = people[right]
            lightest = people[left]

            if heaviest + lightest <= limit:
                left += 1
            right -= 1
            ans += 1
        return ans 



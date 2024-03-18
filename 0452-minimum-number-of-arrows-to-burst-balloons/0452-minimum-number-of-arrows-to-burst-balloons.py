class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        # point = sorted(points, key=lambda x: x[1])
        shot = points[0][1]
        ans = 1
        print(points)
        for start, end in points[1:]:
            if shot < start:
                ans += 1
                shot = end
        return ans
                
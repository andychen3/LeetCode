class DetectSquares:

    def __init__(self):
        self.points = Counter()

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1
        

    def count(self, point: List[int]) -> int:
        ans = 0
        x, y = point
        for (x1, y1), count in self.points.items():
            if abs(x - x1) == 0 or abs(x - x1) != abs(y - y1):
                continue
            ans += count * self.points[(x, y1)] * self.points[(x1, y)]
        return ans


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
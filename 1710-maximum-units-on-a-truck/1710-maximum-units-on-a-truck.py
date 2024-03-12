class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        print(boxes)
        ans = 0
        i = 0
        
        while truckSize and i < len(boxes):
            if boxes[i][0] <= truckSize:
                ans += (boxes[i][0] * boxes[i][1])
                truckSize -= boxes[i][0]
                i += 1
            else:
                ans += (boxes[i][1] * truckSize)
                truckSize -= truckSize
        return ans
            
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxes = sorted(boxTypes, key=lambda x:x[1], reverse=True)
        i = 0
        ans = 0
        
        while truckSize and i < len(boxes):
            if boxes[i][0] <= truckSize:
                truckSize -= boxes[i][0]
                ans += (boxes[i][0] * boxes[i][1])
                i += 1
            else:
                ans += (boxes[i][1] * truckSize)
                return ans
        return ans
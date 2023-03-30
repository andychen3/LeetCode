class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        by_units = sorted(boxTypes, key=lambda x:-x[1])
        size = truckSize
        total = 0
        
        for num_boxes, units in by_units:
            boxes = min(size, num_boxes)
            total += boxes*units
            size -= boxes
            
        return total
            
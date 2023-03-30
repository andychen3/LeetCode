class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        by_units = sorted(boxTypes, key=lambda x:-x[1])
        size = 0
        total = 0
        
        for num_boxes, units in by_units:
            if truckSize - size - num_boxes >= 0:
                size += num_boxes
                total += num_boxes*units
            elif truckSize - size < num_boxes:
                remainder = truckSize - size
                if remainder <= num_boxes:
                    total += remainder*units
                    break
        return total
            
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        total_units = 0
        total_boxes = 0
        
        for boxes in boxTypes:
            num_boxes = boxes[0]
            unit_per_box = boxes[1]
            difference = truckSize-total_boxes
            
            if difference >= num_boxes:
                total_boxes += num_boxes
                total_units += num_boxes*unit_per_box
            else:
                total_units += difference*unit_per_box
                total_boxes += difference
            
            if total_boxes == truckSize:
                return total_units
        return total_units
        

        
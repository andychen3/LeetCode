class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # Sorted the boxes based on the maximum amount of units they have
        boxes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        total = 0

        for num_box, units in boxes:
            if truckSize == 0:
                return total
            # If num_box is within the truckSize limit take all of them
            if num_box <= truckSize:
                truckSize -= num_box
                total += num_box * units
            else:
                # There are more num_boxes then truckSize so take only the amount you can fit on
                # the truck
                total += truckSize * units
                truckSize -= truckSize
            
        return total
            

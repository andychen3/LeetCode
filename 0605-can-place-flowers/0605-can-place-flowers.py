class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        copy_flower_bed = flowerbed
        
        for index in range(len(copy_flower_bed)-1):
            if index == 0 and copy_flower_bed[index] == 0 and copy_flower_bed[index+1] == 0:
                copy_flower_bed[index] = 1
                n -= 1
            elif copy_flower_bed[index-1] == 1 or copy_flower_bed[index+1] == 1:
                continue
            elif copy_flower_bed[index] == 0:
                copy_flower_bed[index] = 1
                n -= 1
            
        if copy_flower_bed[len(copy_flower_bed)-1] == 0 and copy_flower_bed[len(copy_flower_bed)-2] == 0:
            n-=1
        if n > 0:
            return False
        return True
                
            
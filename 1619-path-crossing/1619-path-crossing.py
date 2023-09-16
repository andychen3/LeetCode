class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # What did I do wrong?
        # I forgot that if you move in opposite directions right away you end up in same location.
        # I didn't think to make it a coord and add it to a set and check if the set had the same coord
        hash_set = {(0,0)}
        r,c = (0,0)
        for direction in path:
            if direction == "N":
                r -= 1
            elif direction == "S":
                r += 1
            elif direction == "W":
                c -= 1
            elif direction == "E":
                c += 1
            if (r,c) in hash_set:
                return True
            hash_set.add((r,c))

        return False
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        
        for rock in asteroids:
            if mass < rock:
                return False
            mass += rock
        return True
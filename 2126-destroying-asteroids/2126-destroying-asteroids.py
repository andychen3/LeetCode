class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        
        for rock in asteroids:
            if mass >= rock:
                mass += rock
            else:
                return False
        return True
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        # How can you tell if this is a greedy problem?
        # Because you can rearrange the asteroid in any order and you only want to collide
        # with asteroids that are smaller than the mass so you can gain it to destory the next ones
        # Reasoning is if you can't destroy an asteroid once its sorted decreasing order than all 
        # asteroids after will destory your planet

        asteroids.sort()
        for rock in asteroids:
            if rock <= mass:
                mass += rock
            else:
                return False
        return True
        
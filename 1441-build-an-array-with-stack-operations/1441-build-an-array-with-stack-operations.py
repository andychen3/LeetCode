class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        arr = []
        i = 0
        pointer = 1

        while i < n:
            if i < len(target) and target[i] == pointer:
                arr.append("Push")
                i += 1    
            else:
                arr.append("Push")
                arr.append("Pop")
            pointer += 1
            if pointer > n or i >= len(target):
                break

        return arr
        
        
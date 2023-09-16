class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        source_set = set()
        dest_set = set()

        for source, dest in paths:
            source_set.add(source)
            dest_set.add(dest)
        
        for dest in dest_set:
            if dest not in source_set:
                return dest

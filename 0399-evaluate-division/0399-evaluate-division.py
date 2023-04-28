from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def answer_query(start, end):
            if start not in graph:
                return -1
            
            stack = [(start, 1)]
            seen = {start}
            
            while stack:
                node, ratio = stack.pop()
                if node == end:
                    return ratio
                
                for neighbors in graph[node]:
                    if neighbors not in seen:
                        seen.add(neighbors)
                        stack.append((neighbors, ratio * graph[node][neighbors]))
            return -1
        
        
        # build the graoh
        graph = defaultdict(dict)
        for i in range(len(equations)):
            numerator, denominator = equations[i]
            val = values[i]
            graph[numerator][denominator] = val
            graph[denominator][numerator] = 1/ val
            
        # iteratre through the queries to solve
        ans = []
        
        for numerator, denominator in queries:
            ans.append(answer_query(numerator, denominator))
        return ans
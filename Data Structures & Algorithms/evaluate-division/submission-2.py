from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        bidirectional_weighted_graph = defaultdict(dict)
        bwg = bidirectional_weighted_graph
        for i in range(len(equations)):
            first, second = equations[i]
            bwg[first][second] = values[i]
            bwg[second][first] = 1/values[i]

        def dfs(curr, goal, curr_ratio, visited):
            if curr in visited or curr not in bwg:
                return -1.0
            visited.add(curr)
            if curr == goal:
                return curr_ratio
            output = -1.0
            for neigh in bwg[curr]:
                output = dfs(neigh, goal, curr_ratio * bwg[curr][neigh], visited)
                if output != -1.0:
                    return output
            return output 

        # output = []
        # for query in queries:
        #     start, goal = query
        #     output.append(dfs(start, goal, 1.0, set()))
        # return output

        return [dfs(query[0],query[1], 1.0, set()) for query in queries]
            
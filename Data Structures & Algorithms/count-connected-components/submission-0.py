class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # build an adjecency list
        # for every component not seen run explore
        # count the number of components you need to run explore
        # return the count of components
        adj_list = [[] for i in range(n)]
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        def explore(node):
            # is not in bounds or you seen it already -> return
            if node in seen:
                return
            seen.add(node)
            # run dfs on all neighbors
            for neigh in adj_list[node]:
                explore(neigh)
            return

        seen = set()
        cc_num = 0
        for node, neighbors in enumerate(adj_list):
            if node not in seen:
                explore(node)
                cc_num += 1
        return cc_num
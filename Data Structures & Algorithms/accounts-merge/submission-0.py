from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        bidirectional_graph = defaultdict(set)
        bg = bidirectional_graph
        for account in accounts:
            name = account[0]
            emails = account[1:]
            for i in range(len(emails)):
                bg[emails[i]].add(emails[i])
                if i == 0:
                    continue
                bg[emails[i]].add(emails[i - 1])
                bg[emails[i - 1]].add(emails[i])
        # for key, value in bg.items():
        #     print("key:", key)
        #     for v in value:
        #         print("\tvalue:", v)
        def dfs(curr, visited):
            if curr in visited:
                return visited
            visited.add(curr)
            for neigh in bg[curr]:
                dfs(neigh, visited)
            return visited
        seen = set()  
        output = []
        for account in accounts:
            name = account[0]
            start = account[1]
            if start in seen:
                continue
            set_emails = dfs(start, set())
            seen.update(set_emails)
            sorted_emails = sorted(list(set_emails))
            output.append([name] + sorted_emails)
        return output
            
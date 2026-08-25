from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:        
        adjecency_list = [ [] for i in range(numCourses)]
        in_degree = [ 0 for i in range(numCourses)]
        for course, prereq in prerequisites:
            adjecency_list[prereq].append(course)
            in_degree[course] += 1
        
        valid_starts = []
        for course, prereq_count in enumerate(in_degree):
            if prereq_count == 0:
                valid_starts.append(course)
        
        seen = set()
        queue = deque(valid_starts)
        while queue:
            course = queue.popleft()
            seen.add(course)
            for dependent_course in adjecency_list[course]:
                in_degree[dependent_course] -= 1
                if in_degree[dependent_course] == 0 and not dependent_course in seen:
                    queue.append(dependent_course)
        
        return len(seen) == numCourses
                

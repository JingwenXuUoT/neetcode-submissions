class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # onstruct adjacent list
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        visited = 0 # count poped nodes
        while queue:
            course = queue.popleft()
            visited+=1
            for nxt in graph[course]:
                # reduce its neightbors's in-degree
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
        
        return visited == numCourses
        
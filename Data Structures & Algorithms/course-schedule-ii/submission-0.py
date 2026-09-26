class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # detect cycle in a directed graph
        # if no cycle, return a valid ordering 
        # Topological Sort, the grpah must be acyclic, the rerequisite of a course is the parent node of that course
        # only append the node whose indegree is 0 or becomes 0 during BFS to result
        # return false if the result array len is less than the number of courses
        # res = []
        # indegrees = defaultdict(int)
        # for course, pre in prerequisites:
        #     # did not include any course that do not need a prereq
        #     indegrees[course] += 1
        
        # queue = deque()
        # for pre, indegree in indegrees.items():
        #     if indegree == 0:
        #         queue.append(pre)
        
        # while queue:
        #     pre = queue.popleft()
        #     res.append(pre)
        #     for pre_child in prerequisites[pre]:
        #         # need to create a mapping for each course to its prereqs
        #         indegrees[pre_child] -= 1
        #         if indegrees[pre_child] == 0:
        #             queue.add(pre_child)
        
        # return res if len(res) == numCourses else []
        # # O(V+E)
        graph = defaultdict(list) # prereq to its child course
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        queue = deque([c for c in range(numCourses) if indegree[c] == 0])
        res = []

        while queue:
            node = queue.popleft()
            res.append(node)
            for nxt in graph[node]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
        
        return res if len(res) == numCourses else []

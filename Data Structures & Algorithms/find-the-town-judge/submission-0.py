class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # the judge node has indegree n-1, outdegree 0
        indegree = defaultdict(int)
        outdegree = defaultdict(int)
        for i, j in trust:
                outdegree[i] += 1
                indegree[j] += 1
        for i in range(1, 1+n):
            if indegree[i] == n-1 and outdegree[i] == 0:
                return i
        return -1
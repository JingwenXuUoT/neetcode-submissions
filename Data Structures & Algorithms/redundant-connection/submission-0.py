class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # an undirected graph with n nodes and n edges must contain at lest one cycle
        # need to decide whether the current edge forms a cycle
        # Union-Find algo, create the graph from the given edge lists
        # when connecting the edges, if failed to connect one edge, this edge creates a cycle
        # creates an instance of the DFU object, traverse through the given edges. If the union function returns false, then the current edge forms a cycle
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

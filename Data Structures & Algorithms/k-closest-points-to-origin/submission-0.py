class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for x, y in points:
            distance = -(x**2 + y**2) # heapq is minheap by default
            heapq.heappush(max_heap, [distance, x, y])
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        res = []
        while max_heap:
            distance, x, y = heapq.heappop(max_heap)
            res.append([x,y])
        
        return res
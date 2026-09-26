class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
            
        # convert map items to (-value, key) tuples for a maxheap
        min_heap = []
        for num in frequency.keys():
            heapq.heappush(min_heap, (frequency[num], num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(min_heap)[1])

        return res
        
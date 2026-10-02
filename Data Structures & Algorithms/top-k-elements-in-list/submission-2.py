class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
            
        # convert map items to (-value, key) tuples for a maxheap
        min_heap = []
        for num in frequency.keys():
            heapq.heappush(min_heap, (frequency[num], num)) # elements are compared position by position, first compare index 0 values, if there's a tier, use the second value
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        res = []
        while min_heap:
            res.append(heapq.heappop(min_heap)[1])

        return res
        
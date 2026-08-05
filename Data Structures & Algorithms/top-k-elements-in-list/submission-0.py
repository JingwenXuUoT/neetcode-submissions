class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        # convert map items to (-value, key) tuples for a maxheap
        max_heap = [(-value, key) for key, value in frequency.items()]
        heapq.heapify(max_heap) # heap transformation in-place

        res = []
        for _ in range(k):
            neg_count, num = heapq.heappop(max_heap)
            res.append(num)

        return res
        
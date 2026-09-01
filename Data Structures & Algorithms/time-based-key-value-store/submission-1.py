class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
            
        pv = self.time_map[key] # no need to loop over the whole map
        left = 0
        right = len(pv) - 1
        res = ""
        # should track left, because we are finding the the rightmost timestamp that not exceeding target
        # and when there's no valid answer, should return ""
        while left <= right:
            mid = left + (right - left) // 2
            if pv[mid][0] <= timestamp:
                res = pv[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return res

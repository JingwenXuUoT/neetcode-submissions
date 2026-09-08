class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        last_idx = {}
        for i, ch in enumerate(s):
            last_idx[ch] = i
        
        size = 0
        end = 0
        for i, ch in enumerate(s):
            size += 1
            end = max(end, last_idx[ch])

            if i == end:
                res.append(size)
                size = 0
        
        return res
        
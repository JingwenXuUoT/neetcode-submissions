class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # calculate new slot for each wheel
        initial = "0000"
        if initial in deadends:
            return -1
        if target == "0000":
            return 0

        # each move turning one wheel one slot
        # BFS, find the minimum path to target, avoid 
        res = 0
        queue = deque()
        visited = set(deadends)
        queue.append(initial)
        visited.add(initial)
 
        while queue:
            size = len(queue)
            res += 1
            for _ in range(size):
                cur = queue.popleft()
                # try +1 and -1 for all 4 wheels
                for i in range(4):
                    for j in [1,-1]:
                        digit = str((int(cur[i]) + j) % 10)
                        new = cur[:i] + digit + cur[i+1:]
                        if new in visited:
                            continue
                        if new == target:
                            return res
                        queue.append(new)
                        visited.add(new)
        return -1
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # backtrack, carry local subset constructed sofar to the next recusion
        # maintain a global res array, append the local subset when reaching the leaves of the recursive tree

        res = []

        def dfs(subset, i):
            nonlocal res
            if i == len(nums):
                res.append(subset.copy())
                # the .copy() matters here specifically because subset is the same mutable list object throughout the whole recursion; without copying, every entry in res would just be a reference to that one list, and by the time recursion finishes, they'd all reflect its final (probably empty) state. Copying at the moment of recording freezes a snapshot.
                return
            
            # dfs(subset.append(nums[i]), i+1)   # broken: passes append()'s RETURN VALUE as the argument
            
            subset.append(nums[i]) # fine: runs append() for its side effect, return value ignored
            dfs(subset, i+1) # passes the variable `subset` itself — same list, now mutated
            subset.pop()

            dfs(subset, i+1)

        dfs([], 0)
        return res
        
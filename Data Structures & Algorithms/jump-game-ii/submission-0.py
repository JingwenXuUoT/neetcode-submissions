class Solution:
    def jump(self, nums: List[int]) -> int:
        l = 0
        r = 0
        fartheset = l
        step = 0
        while r < len(nums)-1:
            step += 1
            for idx in range(l, r+1):
                # determine the fartheset index that can be reached from the current range
                fartheset = max(fartheset, idx+nums[idx])
            l = r+1
            r = fartheset
        return step

'''
i =     0 1 2 3 4 5
nums = [2,4,1,1,1,1]
len=6
l=0,1,3
r=0,2,5
far=2,5,
step=1,2,3
'''
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def recurse(path_sum, path, res, i):
            if path_sum == target:
                res.append(path.copy())
                return
            if path_sum > target:
                return
            
            for j in range(i,len(nums)):
                path_sum += nums[j]
                path.append(nums[j])
                recurse(path_sum, path, res, j)
                path.pop()
                path_sum -= nums[j] # remember to subtract this!!

            return

        res = []
        path = []
        recurse(0, path, res, 0)
        
        return res
        
        

        

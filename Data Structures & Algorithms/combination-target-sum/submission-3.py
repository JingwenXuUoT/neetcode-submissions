class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def recurse(path_sum, path, res, i):
            if path_sum == target:
                res.append(path.copy())
                return
            
            for j in range(i,len(nums)):
                if path_sum > target:
                    break
                path.append(nums[j])
                recurse(path_sum+nums[j], path, res, j)
                path.pop()
                # path_sum -= nums[j] # remember to subtract this!!
                # the above line is not needed if the value of path_sum is not actually altered, the +nums[j] is just an add-on

            return

        res = []
        path = []
        recurse(0, path, res, 0)
        
        return res
        
        

        

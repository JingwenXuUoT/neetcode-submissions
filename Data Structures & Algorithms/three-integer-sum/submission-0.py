class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for idx, num in enumerate(nums):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            target = -num

            i = idx+1
            twosum_set = set()
            seen_in_inner = set()
            while(i<len(nums)):
                complement = target - nums[i]
                if complement in twosum_set and (nums[i], complement) not in seen_in_inner:
                    res.add(tuple(sorted([num, nums[i], complement])))
                    seen_in_inner.add((nums[i], complement))
                else:
                    twosum_set.add(nums[i])
                i+=1

        return [list(x) for x in res]
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set() # res is a set to store tuples
        nums.sort() # avoid duplicate nums[i]
        for idx, num in enumerate(nums):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue # avoid duplicate nums[i]
            target = -num

            i = idx+1
            twosum_set = set()
            seen_in_inner = set()
            while(i<len(nums)):
                complement = target - nums[i]
                if complement in twosum_set and (nums[i], complement) not in seen_in_inner:
                    res.add(tuple([num, nums[i], complement]))
                    seen_in_inner.add((nums[i], complement))
                    # the ablove two lines avoids duplicate two sum pair
                else:
                    twosum_set.add(nums[i])
                i+=1

        return [list(x) for x in res]
    
    # a set can store tuples, but cannot store lists
    # because sets only accept hashable(immutable) items
    # tuples are immutable and can be hashed, while lists are mutalble and unhashable
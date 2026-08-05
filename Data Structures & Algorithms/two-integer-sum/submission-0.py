class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for index, num in enumerate(nums):
            i = map.get(target-num, -1)
            if i != -1:
                return [i, index]
            else:
                map[num] = index
        return None
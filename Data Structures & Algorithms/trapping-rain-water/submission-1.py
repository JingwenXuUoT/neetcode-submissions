class Solution:
    def trap(self, height: List[int]) -> int:
        # trap[i] = min(height[l], height[r]) - height[i], where l and r are the greater height element to the left and right of the current position
        # finding l and r for each i is redundant
        # can construct the prefix max and surfix max for each i
        if not height:
            return 0
        prefixMax = []
        surfixMax = []
        premax = height[0]
        surmax = height[len(height)-1]
        for h in height:
            prefixMax.append(premax)
            premax = max(premax, h)
        for h in height[::-1]:
            surfixMax.append(surmax)
            surmax = max(surmax, h)
        surfixMax = surfixMax[::-1]

        traps = []
        for i in range(len(height)):
            traps.append(min(surfixMax[i], prefixMax[i]) - height[i])
        
        res = 0
        for trap in traps:
            res += max(0, trap)
        
        return res
        # O(n), O(n)
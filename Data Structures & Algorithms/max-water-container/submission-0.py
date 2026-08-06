class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        i = 0
        j = len(heights)-1
        
        # iheight_max = heights[0]
        # jheight_max = heihgts[len(heights)-1]

        while(i<j):
            area = (j-i) * min(heights[i], heights[j])
            max_area = max(max_area, area)
            if(heights[i] < heights[j]):
                i+=1
            else:
                j-=1
        
        return max_area
        
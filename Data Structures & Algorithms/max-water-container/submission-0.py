class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        maxarea = 0
        while (l < r):
            tall = min(heights[l], heights[r])
            width = r - l
            area = tall*width
            maxarea = max(maxarea, area)
            if (heights[l] > heights[r]):
                r-=1
            
            else:
                l+=1

        return maxarea

         
        
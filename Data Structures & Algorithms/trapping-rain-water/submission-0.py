class Solution:
    def trap(self, height: List[int]) -> int:
        leftmaxes = []
        rightmaxes = []
        currentmax = 0
        for num in height:
          currentmax = max(currentmax, num)
          leftmaxes.append(currentmax)

        currentmax = 0
        for num in height[::-1]:
            currentmax = max(currentmax, num)
            rightmaxes.append(currentmax)
        
        rightmaxes = rightmaxes[::-1]
        water = 0

        for i in range(len(height)):
            if min(leftmaxes[i], rightmaxes[i]) - height[i] < 0:
                continue
            else:
                water += (min(leftmaxes[i], rightmaxes[i]) - height[i])
        print("height:     ", height)
        print("leftmaxes:  ", leftmaxes)
        print("rightmaxes: ", rightmaxes)
        return water
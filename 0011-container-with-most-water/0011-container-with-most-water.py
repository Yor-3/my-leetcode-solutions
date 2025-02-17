class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        maxres = 0
        left = 0
        right = len(height)-1
        while left<right:
            res = (right-left)*(min(height[left],height[right]))

            maxres = max(res,maxres)

            if height[left]<height[right]:
                left+=1
            else:
                right = right-1

        return maxres
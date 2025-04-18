class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l,r = 0,len(height)-1
        lmax,rmax = height[l],height[r]

    
        while l<r:
            if lmax<=rmax:
                l+=1
                lmax = max(lmax,height[l])
                res+= max(0,lmax-height[l])

            else:
                r-=1
                rmax = max(rmax,height[r])
                res+=max(0,rmax-height[r])

        return res
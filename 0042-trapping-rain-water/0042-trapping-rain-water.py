class Solution:
    def trap(self, height: List[int]) -> int:
        max_height = max(height)
        max_height_index= height.index(max_height)

        curr_height = 0
        volume=0
        for i in range(max_height_index):
            if height[i]>= curr_height:
                curr_height = height[i]
            else:
                volume += curr_height - height[i]

        curr_height = 0
        

        for i in range(len(height)-1, max_height_index,-1):
            if height[i] >= curr_height:
                curr_height =height[i] 
            else:
                volume +=curr_height - height[i]

        return volume

                


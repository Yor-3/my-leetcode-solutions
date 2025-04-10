class Solution:
    def continuousSubarrays(self, nums):
        n = len(nums)
        left = 0
        range_min = float('inf')
        range_max = float('-inf')

        count = 0
        right = 0

        for right in range(n):
            range_min = min(range_min, nums[right])
            range_max = max(range_max, nums[right])

            if range_max - range_min > 2:
                win_size = right - left
                count += (win_size * (win_size + 1)) // 2

                left = right
                # Expand current window to as left as possible
                range_min = nums[right]
                range_max = nums[right]
                while left > 0 and abs(nums[right] - nums[left - 1]) <= 2:
                    left -= 1
                    range_min = min(range_min, nums[left])
                    range_max = max(range_max, nums[left])

                # Subtract overcounted subarrays
                if left < right:
                    win_size = right - left
                    count -= (win_size * (win_size + 1)) // 2

        # Add subarrays from the last window
        win_size = right - left+1
        count += (win_size * (win_size + 1)) // 2

        return count
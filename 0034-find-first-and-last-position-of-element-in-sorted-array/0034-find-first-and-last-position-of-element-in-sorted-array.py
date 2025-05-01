class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(findFirst):
            low, high = 0, len(nums) - 1
            index = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    index = mid
                    if findFirst:
                        high = mid - 1  # move left
                    else:
                        low = mid + 1   # move right
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return index

        return [binarySearch(True), binarySearch(False)]

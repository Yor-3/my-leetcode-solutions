from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        myset = set()  # Use a set for efficiency
        for num in nums:
            if num in myset:
                return True  # Found a duplicate
            myset.add(num)  # Add the number to the set
        return False  # No duplicates found

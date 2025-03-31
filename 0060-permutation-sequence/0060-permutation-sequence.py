class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        import math

        # Create the list of numbers to use
        nums = list(range(1, n + 1))
        
        # Convert k to 0-based index
        k -= 1  
        
        res = ""
        
        # Build the k-th permutation
        for i in range(n, 0, -1):
            fact = math.factorial(i - 1)   # (n-1)!
            
            # Find the index of the current digit
            index = k // fact  
            
            # Append the selected digit
            res += str(nums[index])
            
            # Remove the used digit
            nums.pop(index)
            
            # Update k for the next iteration
            k %= fact
        
        return res

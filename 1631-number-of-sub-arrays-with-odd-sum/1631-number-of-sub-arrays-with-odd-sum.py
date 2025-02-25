class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        res = 0
        odd= 0 
        even =  0
        cur = 0
        MOD = 10**9+7

        for n in arr:
            cur+=n
            if cur%2==0:
                res = (res+odd)%MOD
                even +=1
            else:
                res= (res+even+1)%MOD
                odd +=1

        return res
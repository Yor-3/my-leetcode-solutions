class Solution:
    def countLargestGroup(self, n: int) -> int:
        hash = defaultdict(int)
        def findsum(i):
            if i ==0:
                return 0

            sum=0
            while i>0:
                sum+=i%10
                i//=10

            return sum

        for i in range(1,n+1):
            hash[findsum(i)] +=1

        maxsize = max(hash.values())

        count = sum(1 for v in hash.values() if v == maxsize)

        return count

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        lps = [0]*len(needle)


        i ,j=1,0

        while i< len(needle):
            if needle[i]==needle[j]:
                j+=1
                lps[i] = j
                i+=1

            else:
                if j!=0:
                    j = lps[j-1] 

                else:
                    lps[i]=0
                    i+=1

        i=j=0

        while i<len(haystack):

            if haystack[i]==needle[j]:
                i+=1
                j+=1

                if j==len(needle):
                    return i-j

            else:
                if j!=0:
                    j = lps[j-1]


                else:
                    i+=1


        return -1

            
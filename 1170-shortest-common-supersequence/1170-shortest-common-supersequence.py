class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # Compute the LCS using Hirschberg's algorithm.
        lcs = self.hirschberg(str1, str2)
        # Merge str1 and str2 using the LCS as a guide.
        return self.mergeSCS(str1, str2, lcs)

    def mergeSCS(self, s1: str, s2: str, lcs: str) -> str:
        i, j = 0, 0
        res = []
        # For each character in the LCS, append characters from s1 and s2
        # that come before the matching character.
        for c in lcs:
            while i < len(s1) and s1[i] != c:
                res.append(s1[i])
                i += 1
            while j < len(s2) and s2[j] != c:
                res.append(s2[j])
                j += 1
            # Append the common character and move past it in both strings.
            res.append(c)
            i += 1
            j += 1
        # Append any remaining parts.
        res.append(s1[i:])
        res.append(s2[j:])
        return "".join(res)

    def hirschberg(self, A: str, B: str) -> str:
        # Base case: if A is empty, LCS is empty.
        if len(A) == 0:
            return ""
        # Base case: if A is of length 1, check if its character appears in B.
        if len(A) == 1:
            return A if A in B else ""
        
        # Divide A into two halves.
        i = len(A) // 2
        # Compute the LCS length for the left half.
        L1 = self.lcsLength(A[:i], B)
        # Compute the LCS length for the right half on reversed strings.
        L2 = self.lcsLength(A[i:][::-1], B[::-1])
        
        # Find the index k in B that maximizes L1[k] + L2[len(B) - k]
        max_val = -1
        k = 0
        for j in range(len(B) + 1):
            if L1[j] + L2[len(B) - j] > max_val:
                max_val = L1[j] + L2[len(B) - j]
                k = j
        
        # Recursively compute the LCS for the two halves.
        LCS_left = self.hirschberg(A[:i], B[:k])
        LCS_right = self.hirschberg(A[i:], B[k:])
        return LCS_left + LCS_right

    def lcsLength(self, A: str, B: str) -> list:
        """
        Compute the LCS DP array for A and B using only O(len(B)) space.
        Returns an array dp of length len(B)+1 where dp[j] is the length of the
        LCS of A and B[:j].
        """
        dp = [0] * (len(B) + 1)
        for a in A:
            new_dp = [0] * (len(B) + 1)
            for j in range(len(B)):
                if a == B[j]:
                    new_dp[j + 1] = dp[j] + 1
                else:
                    new_dp[j + 1] = max(new_dp[j], dp[j + 1])
            dp = new_dp
        return dp
from bisect import bisect_left
from collections import defaultdict

class SegmentTree:
    def __init__(self, size):
        self.tree = [(-1, 0)] * (4 * size)
    
    def _merge(self, a, b):
        if a[0] == b[0]:
            return (a[0], a[1] + b[1])
        return max(a, b)

    def update(self, index, l, r, pos, val):
        if l == r:
            if self.tree[index][0] == val[0]:
                self.tree[index] = (val[0], self.tree[index][1] + val[1])
            else:
                self.tree[index] = max(self.tree[index], val)
            return
        mid = (l + r) // 2
        if pos <= mid:
            self.update(2 * index, l, mid, pos, val)
        else:
            self.update(2 * index + 1, mid + 1, r, pos, val)
        self.tree[index] = self._merge(self.tree[2 * index], self.tree[2 * index + 1])

    def query(self, index, l, r, ql, qr):
        if ql > r or qr < l:
            return (-1, 0)
        if ql <= l and r <= qr:
            return self.tree[index]
        mid = (l + r) // 2
        left = self.query(2 * index, l, mid, ql, qr)
        right = self.query(2 * index + 1, mid + 1, r, ql, qr)
        return self._merge(left, right)

class Solution:
    def findNumberOfLIS(self, nums):
        sorted_unique = sorted(set(nums))
        compress = {num: i for i, num in enumerate(sorted_unique)}
        n = len(sorted_unique)
        st = SegmentTree(n)

        for num in nums:
            idx = compress[num]
            max_len, count = st.query(1, 0, n - 1, 0, idx - 1)
            if max_len == -1:
                max_len = 0
                count = 1
            st.update(1, 0, n - 1, idx, (max_len + 1, count))

        return st.tree[1][1]

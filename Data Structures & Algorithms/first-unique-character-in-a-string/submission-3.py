class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        count = defaultdict(int)
        for i, c in enumerate(s):
            if c in count:
                count[c] = n
            else:
                count[c] = i


        res = n
        for c in s:
            res = min(res, count[c])

        return -1 if n == res else res
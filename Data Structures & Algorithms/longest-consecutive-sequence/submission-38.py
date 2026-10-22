class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 0
        res = 0
        nSet = set(nums)
        for n in nums:
            if (n - 1) not in nSet:
                length = 1
                while (n + length) in nSet:
                    length += 1
                res = max(length, res)

        return res
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nset = set(nums)

        for n in nums:
            if (n - 1) not in nset:
                length = 1
                while (n + length) in nset:
                    length += 1
                longest = max(longest, length)

        return longest
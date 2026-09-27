class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nSet = set(nums)

        for n in nums:
            if (n - 1) not in nSet:
                length = 1
                while (n + length) in nSet:
                    length += 1
                longest = max(longest, length)

        return longest
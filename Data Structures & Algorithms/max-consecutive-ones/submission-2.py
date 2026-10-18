class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        length = 0
        maxL = 0

        for n in nums:
            if n == 1:
                length += 1
            else:
                maxL = max(maxL, length)
                length = 0
        return max(maxL, length)
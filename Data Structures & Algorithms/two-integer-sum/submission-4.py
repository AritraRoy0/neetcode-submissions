class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indecies = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in indecies:
                return [indecies[complement], i]
            indecies[num] = i
        
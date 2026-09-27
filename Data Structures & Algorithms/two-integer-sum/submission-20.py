class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indecies = {}

        for i, n in enumerate(nums):
            comp = target - n

            if comp in indecies:
                return [indecies[comp], i]
            indecies[n] = i
            
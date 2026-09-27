class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indecies = {}

        for i, n in enumerate(nums):
            complement = target - n
            if complement in indecies:
                return [indecies[complement], i]
            indecies[n] = i


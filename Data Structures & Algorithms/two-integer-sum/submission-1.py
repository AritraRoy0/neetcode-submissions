class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indecies = {}

        for i, num in enumerate(nums):
            compl = target - num
            if compl in indecies.keys():
                return [indecies[compl], i]
            indecies[num] = i
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indecies = {}

        for i, num in enumerate(nums):
            compliment = target - num

            if compliment in indecies.keys():
                return [indecies[compliment], i]
            indecies[num] = i

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2
            nm = nums[m]

            if nm == target:
                return m
            elif nm < target:
                l = m + 1
            else:
                r = m - 1

        return -1
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2 and nums[0] + nums[1] == target:
            return [0, 1]

        view = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in view:
                return [i, view[diff]]
            else:
                view[nums[i]] = i

        return []

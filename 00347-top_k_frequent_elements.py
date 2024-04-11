from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums

        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        sorted = [[] for _ in range(len(nums) + 1)]

        for key, val in counts.items():
            sorted[val].append(key)

        results = []

        for idx in reversed(sorted):
            for num in idx:
                results.append(num)

                if len(results) == k:
                    return results

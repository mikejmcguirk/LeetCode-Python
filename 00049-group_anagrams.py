from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for str in strs:
            letters = [0] * 26

            for char in str:
                letters[ord(char) - ord("a")] += 1

            groups[tuple(letters)].append(str)

        return list(groups.values())

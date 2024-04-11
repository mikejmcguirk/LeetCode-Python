class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        if len(s) == 1 and (s[0] != t[0]):
            return False

        letters = [0] * 26
        SUBTRACTOR = ord("a")

        for i in range(len(s)):
            s_char = ord(s[i]) - SUBTRACTOR
            t_char = ord(t[i]) - SUBTRACTOR

            letters[s_char] += 1
            letters[t_char] -= 1

        for letter in letters:
            if letter != 0:
                return False

        return True

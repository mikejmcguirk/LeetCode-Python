class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        if len(s) == 1 and (s != t):
            return False

        if s == t:
            return True

        # Only lower-case english letters are possible. A hash-based solution is not needed
        letters = [0] * 26
        SUBTRACTOR = 97

        for i in range(len(s)):
            s_char = ord(s[i]) - SUBTRACTOR
            t_char = ord(t[i]) - SUBTRACTOR

            letters[s_char] += 1
            letters[t_char] -= 1

        for letter in letters:
            if letter != 0:
                return False

        return True

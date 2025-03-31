class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = list(s)
        t_chars = list(t)

        s_chars.sort()
        t_chars.sort()

        return s_chars == t_chars
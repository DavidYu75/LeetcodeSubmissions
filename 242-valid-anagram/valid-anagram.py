class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_count = {}

        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        for char in t:
            if char not in char_count or char_count[char] == 0:
                return False
            
            char_count[char] -= 1

        return True
        
        # s_chars = list(s)
        # t_chars = list(t)

        # s_chars.sort()
        # t_chars.sort()

        # return s_chars == t_chars

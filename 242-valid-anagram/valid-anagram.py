class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagram
        # {'a': 2, 'n': 1, 'g': 1, 'r': 1, 'm': 1}
        # 

        if len(s) != len(t):
            return False

        s_map = {}
        for char in s:
            s_map[char] = s_map.get(char, 0) + 1
        
        t_map = {}
        for char in t:
            t_map[char] = t_map.get(char, 0) + 1
        
        return s_map == t_map

        # time: O(n)
        # space: O(n)

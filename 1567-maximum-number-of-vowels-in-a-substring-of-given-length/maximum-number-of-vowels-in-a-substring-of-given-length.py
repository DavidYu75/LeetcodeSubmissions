class Solution:
    # leetcode
    # k = 3
    # time: O(n)
    # space: O(n)
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        char_s = list(s)
        print(char_s)
        char_window = []
        max_vowel_count = 0

        for i in range(k):
            char_window.append(char_s[i])

        for char in char_window:
            if char in vowels:
                max_vowel_count += 1
        
        vowel_count = max_vowel_count

        for i in range(k, len(s)):
            if char_window.pop(0) in vowels:
                vowel_count -= 1
            if char_s[i] in vowels:
                vowel_count += 1

            char_window.append(char_s[i])

            if vowel_count > max_vowel_count:
                max_vowel_count = vowel_count

        return max_vowel_count

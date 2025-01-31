class Solution:
    # time: O(n)
    # space: O(n)
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        char_window = s[:k]
        max_vowel_count = 0

        for char in list(char_window):
            if char in vowels:
                max_vowel_count += 1

        vowel_count = max_vowel_count

        for i in range(k, len(s)):
            if char_window[i - k] in vowels:
                vowel_count -= 1
            if s[i:i+1] in vowels:
                vowel_count += 1

            char_window += s[i:i+1]

            if vowel_count > max_vowel_count:
                max_vowel_count = vowel_count
        
        return max_vowel_count

class Solution:
    # time: O(n)
    # space: O(1)
    def maxVowels(self, s: str, k: int) -> int:
        #vowels = {'a', 'e', 'i', 'o', 'u'}
        # vowels = "aeiou"
        # char_window = s[:k]
        # max_vowel_count = 0

        # for char in list(char_window):
        #     if char in vowels:
        #         max_vowel_count += 1

        # vowel_count = max_vowel_count

        # for i in range(k, len(s)):
        #     if char_window[i - k] in vowels:
        #         vowel_count -= 1
        #     if s[i:i+1] in vowels:
        #         vowel_count += 1

        #     char_window += s[i:i+1]

        #     if vowel_count > max_vowel_count:
        #         max_vowel_count = vowel_count
        
        # return max_vowel_count

        vowels = {'a', 'e', 'i', 'o', 'u'}
        ans = cnt = 0
        for i, c in enumerate(s):
            if c in vowels:
                cnt += 1
            if i >= k and s[i - k] in vowels:
                cnt -= 1
            ans  = max(cnt, ans)
        return ans 

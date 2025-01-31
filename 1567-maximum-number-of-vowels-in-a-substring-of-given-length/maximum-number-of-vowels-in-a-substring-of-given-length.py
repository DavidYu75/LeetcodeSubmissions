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

        # Maximum vowels i.e. ans
        ans: int = 0
            
        # Vowels in current window
        currCount: int = 0
            
        # String of vowels
        vowels: str = "aeiou"
            
        # Using sliding window technique to 
        # calculate number of vowels in each window and 
        # update the count
        for i, v in enumerate(s):
            if i >= k:
                if s[i-k] in vowels:
                    currCount -= 1
            if s[i] in vowels:
                currCount += 1
            ans = max(currCount, ans)
        return ans

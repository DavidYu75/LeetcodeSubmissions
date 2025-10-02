class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length = 0
        longest_string = ""

        for i in range(len(s)):
            # odd length
            left, right = i, i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > max_length:
                    longest_string = s[left:right + 1]
                    max_length = (right - left + 1)

                left -= 1
                right += 1
            
            # even length
            left, right = i, i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > max_length:
                    longest_string = s[left:right + 1]
                    max_length = (right - left + 1)
                
                left -= 1
                right += 1
            
        return longest_string
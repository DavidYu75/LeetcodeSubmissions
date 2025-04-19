import re

class Solution:
    def isPalindrome(self, s: str) -> bool:

        def remove_alphanumeric(text):
            return re.sub(r'[^a-zA-Z0-9]', '', text)

        lowercase_s = s.lower()
        lowercase_s = remove_alphanumeric(lowercase_s)

        first = 0
        last = len(lowercase_s)

        while first < last:
            if lowercase_s[first:first+1] != lowercase_s[last-1:last]:
                return False
            first += 1
            last -= 1
        
        return True
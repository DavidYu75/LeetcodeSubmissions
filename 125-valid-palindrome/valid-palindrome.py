class Solution:
    def isPalindrome(self, s: str) -> bool:
        removed_alpha = ''.join(c for c in s if c.isalnum())
        removed_alpha = removed_alpha.lower()

        left, right = 0, len(removed_alpha) - 1

        while left < right:
            if removed_alpha[left] != removed_alpha[right]:
                return False

            left += 1 
            right -= 1

        return True
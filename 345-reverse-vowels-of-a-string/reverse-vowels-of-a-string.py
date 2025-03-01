class Solution:
    # IceCreAm
    # I e e A
    # AceCreIm

    # leetcode
    # e e o e
    # leotcede
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        vowels_found = []

        for char in s:
            if char in vowels:
                vowels_found.append(char)

        char_s = list(s)

        for i in range(len(char_s)):
            if char_s[i] in vowels:
                char_s[i] = vowels_found.pop()

        return ''.join(char_s)
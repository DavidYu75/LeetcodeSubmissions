class Solution:
    # IceCreAm
    # I e e A
    # AceCreIm

    # leetcode
    # e e o e
    # leotcede
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        # vowels_found = []

        # for char in s:
        #     if char in vowels:
        #         vowels_found.append(char)

        char_s = list(s)

        # for i in range(len(char_s)):
        #     if char_s[i] in vowels:
        #         char_s[i] = vowels_found.pop()

        # return ''.join(char_s)

        first = 0
        last = len(s) - 1

        while first < last:
            if char_s[first] in vowels:
                for i in range(last, first, -1):
                    if char_s[i] in vowels:
                        char_s[first], char_s[i] = char_s[i], char_s[first]
                        last = i - 1
                        break
            first += 1
        
        return ''.join(char_s)
class Solution:
    # IceCreAm
    # I e e A
    # AceCreIm

    # leetcode
    # e e o e
    # leotcede
    def reverseVowels(self, s: str) -> str:
        # vowels_found = []

        # for char in s:
        #     if char in vowels:
        #         vowels_found.append(char)

        # for i in range(len(char_s)):
        #     if char_s[i] in vowels:
        #         char_s[i] = vowels_found.pop()

        # return ''.join(char_s)

        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        first = 0
        last = len(s) - 1

        char_s = list(s)

        # while first < last:
        #     if char_s[first] in vowels:
        #         for i in range(last, first, -1):
        #             if char_s[i] in vowels:
        #                 char_s[first], char_s[i] = char_s[i], char_s[first]
        #                 last = i - 1
        #                 break
        #     first += 1

        while first < last:
            if char_s[first] in vowels and char_s[last] not in vowels:
                last -= 1
            if char_s[first] not in vowels and char_s[last] in vowels:
                first += 1
            if char_s[first] not in vowels and char_s[last] not in vowels:
                first += 1
                last -= 1
            if char_s[first] in vowels and char_s[last] in vowels:
                char_s[first], char_s[last] = char_s[last], char_s[first]
                first += 1
                last -= 1

        
        return ''.join(char_s)
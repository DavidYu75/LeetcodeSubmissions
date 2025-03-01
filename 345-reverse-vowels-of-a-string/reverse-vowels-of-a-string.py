class Solution:
    # IceCreAm
    # I e e A
    # AceCreIm

    # leetcode
    # e e o e
    # leotcede
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        first = 0
        last = len(s) - 1

        char_s = list(s)

        while first < last:
            while first < last and char_s[first] not in vowels:
                first += 1

            while first < last and char_s[last] not in vowels:
                last -= 1

            char_s[first], char_s[last] = char_s[last], char_s[first]

            first += 1
            last -= 1

        
        return ''.join(char_s)
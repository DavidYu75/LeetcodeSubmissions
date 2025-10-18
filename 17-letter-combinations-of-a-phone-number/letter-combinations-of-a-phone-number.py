class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # digits = "23"
        # bf
        # b
        # backtrack
        # every time our combination equals to the length of our digits, we backtrack and use the next available letter that is mapped to our digits
        # hashmap, where each digit maps to its letters O(1)
        # for every letter in our first digit, we will generate all letter combinations with the subsequent letters from our first digit letter
        # abc
        # b

        phone_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        def backtrack(i, curr_comb):
            if len(curr_comb) == len(digits):
                result.append(curr_comb)
                return
            
            for letter in phone_letters[digits[i]]:
                backtrack(i+1, curr_comb + letter)
        
        
        backtrack(0, "")

        return result

        # time: O(4^n)
        # space: O(n)
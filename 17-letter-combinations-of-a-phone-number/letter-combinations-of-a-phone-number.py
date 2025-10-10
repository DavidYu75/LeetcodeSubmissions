class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
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
            
            for c in phone_letters[digits[i]]:
                backtrack(i+1, curr_comb + c)
            
        if digits:
            backtrack(0, "")
        
        return result

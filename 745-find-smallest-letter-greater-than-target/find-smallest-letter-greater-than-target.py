class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # for letter in letters:
        #     if letter > target:
        #         return letter
        
        # return letters[0]
        
        # time: O(n)
        # space: O(1)

        left, right = 0, len(letters) - 1

        while left <= right:
            middle = (left + right) // 2

            if letters[middle] <= target:
                left = middle + 1
            else:
                right = middle - 1
        
        if left == len(letters):
            return letters[0]
        else:
            return letters[left]
        
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1

        while left <= right:
            middle = (left + right) // 2

            if letters[middle] <= target:
                left = middle + 1
            else:
                right = middle - 1
        
        if len(letters) == left:
            return letters[0]
        else:
            return letters[left]
        
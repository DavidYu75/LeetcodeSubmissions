class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left, right = 0, 1
        result = 1
        prev_sign = ""

        while right < len(arr):
            if arr[right - 1] > arr[right] and prev_sign != ">":
                result = max(result, right - left + 1)
                right += 1
                prev_sign = ">"
            elif arr[right - 1] < arr[right] and prev_sign != "<":
                result = max(result, right - left + 1)
                right += 1
                prev_sign = "<"
            else:
                right = right + 1 if arr[right] == arr[right - 1] else right
                left = right - 1
                prev_sign = ""

        return result

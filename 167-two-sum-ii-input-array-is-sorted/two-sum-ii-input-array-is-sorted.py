class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i in range(len(numbers)):
        #     complement = target - numbers[i]
        #     for j in range(i, len(numbers)):
        #         if numbers[j] == complement:
        #             return [i+1, j+1]
        
        # return []

        first = 0
        last = len(numbers) - 1

        while first < last:
            current_sum = numbers[first] + numbers[last]
            if current_sum == target:
                return [first+1, last+1]
            elif current_sum > target:
                last -= 1
            elif current_sum < target:
                first += 1
        
        return []
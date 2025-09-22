class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # we have two pointers. one in the beginning and one in the end
        # check the sum and compare it with target
        # if sum is greater than target, we decrement right pointer
        # if sum is less than target, we increment left pointer
        # 2, 7, 11, 15  target = 9
        # left = 2, right = 15
        # 17 > 9
        # left = 2, right = 11
        # 13 > 9
        # left = 2, right = 7
        # 9 == 9

        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum > target:
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                return [left+1, right+1]
        
        return []
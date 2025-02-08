class Solution:
    # n = 4
    # 0 + 1 + 1 = 2
    # 2 + 2 = 4
    def tribonacci(self, n: int) -> int:
        first_num = 0
        second_num = 1
        third_num = 1

        if n == 0:
            return first_num
         
        if n <= 2:
            return second_num

        for i in range(2, n):
            result = first_num + second_num + third_num
            first_num = second_num
            second_num = third_num
            third_num = result
        
        return result
        
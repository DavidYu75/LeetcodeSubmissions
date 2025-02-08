class Solution:
    # n = 4
    # 0 + 1 + 1 = 2
    # 2 + 2 = 4
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0

        first_num = 0
        second_num = 1
        third_num = 1

        for i in range(n - 2):
            result = first_num + second_num + third_num
            first_num = second_num
            second_num = third_num
            third_num = result
        
        return third_num
        
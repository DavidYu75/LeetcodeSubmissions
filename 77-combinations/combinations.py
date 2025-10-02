class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def combinations(i, curr_set, result, n, k):
            if len(curr_set) == k:
                result.append(curr_set.copy())
                return

            if i > n:
                return

            for j in range(i, n + 1):
                curr_set.append(j)
                combinations(j + 1, curr_set, result, n, k)
                curr_set.pop()

        result, curr_set = [], []
        combinations(1, curr_set, result, n, k)

        return result

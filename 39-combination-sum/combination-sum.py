class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def helper(i, curr_set, curr_total):
            if curr_total == target:
                result.append(curr_set.copy())
                return

            for j in range(i, len(candidates)):
                if curr_total + candidates[j] > target:
                    return

                curr_set.append(candidates[j])
                helper(j, curr_set, curr_total + candidates[j])
                curr_set.pop()

        helper(0, [], 0)

        return result
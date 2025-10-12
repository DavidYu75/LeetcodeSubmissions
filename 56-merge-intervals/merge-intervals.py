class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort our intervals by their starting value
        # go through the intervals array, check the previous interval's ending value with the current interval's starting value
        # compare the ending and starting value, we want to merge by taking the max of both interval's ending value
        # result = contains all the non-overlapping intervals that we want to return
        # result = [intervals[0]]

        intervals.sort(key=lambda pair: pair[0])
        result = [intervals[0]]

        for start, end in intervals[1:]:
            previous_ending = result[-1][1]

            if start <= previous_ending:
                result[-1][1] = max(end, result[-1][1])
            else:
                result.append([start, end])
        
        return result
        
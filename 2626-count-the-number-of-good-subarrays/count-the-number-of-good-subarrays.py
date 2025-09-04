class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        """
        count the number of subarrays of nums having at least k pairs of equal elements
        pairs are index pairs i<j with nums[i] == nums[j]
        """

        # nums = [1, 1, 1, 1, 1]
        # k = 10

        # sliding window and hashmap to maintain the current number of equal pairs in window
        # expand right, shrink left when pairs >= k
        n = len(nums)
        freq = defaultdict(int) # frequency of values in current window
        pairs = 0   # number of equal index-pairs in window
        left = 0
        good_subarrays = 0

        for right, x in enumerate(nums):
            pairs += freq[x]
            freq[x] += 1

            while pairs >= k:
                good_subarrays += n - right
                y = nums[left]

                pairs -= freq[y] - 1
                freq[y] -= 1
                left += 1
        
        return good_subarrays

        # everytime a window has >= k pairs, all the extensions to the right of the window are valid
        # add (n - right) to the answer
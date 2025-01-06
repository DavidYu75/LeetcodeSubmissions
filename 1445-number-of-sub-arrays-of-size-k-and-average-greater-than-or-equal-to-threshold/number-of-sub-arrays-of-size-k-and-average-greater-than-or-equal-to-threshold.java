class Solution {
    // Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
    // Output: 3
    // [2, 2, 2] = 2
    // [2, 2, 2] = 2
    // [2, 2, 5] = 3
    // [2, 5, 5] = 4
    // count++
    // [5, 5, 5] = 5
    // count++
    // [5, 5, 8] = 6
    // count++

    // Time: O(n)
    // Space: O(1)
    public int numOfSubarrays(int[] arr, int k, int threshold) {
        int count = 0;
        int windowAverage = 0;

        for (int i = 0; i < k; i++) {
            windowAverage += arr[i];
        }

        if (windowAverage / k >= threshold) {
            count++;
        }

        for (int i = k; i < arr.length; i++) {
            windowAverage += arr[i] - arr[i - k];
            if (windowAverage / k >= threshold) {
                count++;
            } 
        }

        return count;

    }
}
class Solution {
    // Input: nums = [1,2,3,4]
    // Output: [24,12,8,6]
    // 1 : 2 * 3 * 4 = 24
    // 2 : 1 * 3 * 4 = 12
    // 3 : 1 * 2 * 4 = 8
    // 4 : 1 * 2 * 3 = 6
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int output[] = new int[n];
        Arrays.fill(output, 1);

        int current = 1;
        // 1, 2, 3, 4
        // current = 1
        // i = 0
        // 1, 1, 1, 1
        // current = 1
        // i = 1
        // 1, 1, 1, 1
        // current = 2
        // i = 2
        // 1, 1, 2, 1
        // current = 6
        // i = 3
        // 1, 1, 2, 6
        // current = 24
        for (int i = 0; i < n; i++) {
            output[i] *= current;
            current *= nums[i];
        }

        // 1, 1, 2, 6
        // 1, 1, 2, 6
        // current = 4
        // i = 2
        // 1, 1, 8, 6
        // current = 12
        // i = 1
        // 1, 12, 8, 6
        // current = 24
        // i = 0
        // 24, 12, 8, 6
        current = 1;
        for (int i = n - 1; i >= 0; i--) {
            output[i] *= current;
            current *= nums[i];
        }

        return output;
    }
}
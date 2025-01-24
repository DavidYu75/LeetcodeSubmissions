class Solution {
    public int maxSubArray(int[] nums) {
        int globalMax = Integer.MIN_VALUE;
        int currMax = 0;

        for (int i = 0; i < nums.length; i++) {
            currMax += nums[i];

            globalMax = Math.max(currMax, globalMax);

            if (currMax < 0) {
                currMax = 0;
            }
        }

        return globalMax;
    }
}
class Solution {
    public int maximumWealth(int[][] accounts) {
        int currMax = 0;

        for (int i = 0; i < accounts.length; i++) {
            int currWealth = 0;

            for (int j = 0; j < accounts[i].length; j++) {
                currWealth += accounts[i][j];
            }

            if (currWealth > currMax) {
                currMax = currWealth;
            }
        }

        return currMax;
    }
}
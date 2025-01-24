class Solution {
    // Input: c = 5
    // Output: true
    // 1, 2, 3, 4
    // 5 - 1^2 = 4
    // Time: O(n^2)
    // 1 2 3 4 5
    // sqrt(5)
    // 0 1 2

    
    public boolean judgeSquareSum(int c) {
        // for (int i = 0; i < c + 1; i++) {
        //     int firstSquare = (int) Math.pow(i, 2);
        //     int difference = c - firstSquare;  
        //     for (int j = 0; j < c + 1; j++) {
        //         if ((int) Math.pow(j, 2) == difference) {
        //             return true;
        //         }
        //     }
        // }

        // return false;


        // 8
        // 0 1 2 3 4 5 6 7 8
        // firstPointer = 0
        // secondPointer = 2
        // currentSum = 0^2 + 2^2 = 4
        // first = 1
        // second = 2
        // currentSum = 1^2 + 2^2 = 5
        // first = 2
        // second = 2
        // currentSum = 2^2 + 2^2 = 8
        long firstPointer = 0;
        long secondPointer = (long) Math.sqrt(c);

        while (firstPointer <= secondPointer) {
            long currentSum = firstPointer * firstPointer + secondPointer * secondPointer;
            if (currentSum > c) {
                secondPointer--;
            } else if (currentSum < c) {
                firstPointer++;
            } else {
                return true;
            }
        }

        return false;
    }
}
class Solution {
    public String originalDigits(String s) {
        /**
         * zero 
         * one
         * two
         * three
         * four
         * five
         * six
         * seven
         * eight
         * nine
         * Unique: zero (z), two (w), four (u), six (x), eight (g)
         * Derived: one (o - 0 - 2 - 4), three (h - 8), five (f - 4), seven (s - 6), nine (i - 6 - 8 - 5)
         */

         int[] characters = new int[26];
         for (char c : s.toCharArray()) {
            characters[c - 'a']++;
         }

         int[] number = new int[10];

         number[0] = characters['z'-'a'];
         number[2] = characters['w'-'a'];
         number[4] = characters['u'-'a'];
         number[6] = characters['x'-'a'];
         number[8] = characters['g'-'a'];

         number[1] = characters['o'-'a'] - number[0] - number[2] - number[4];
         number[3] = characters['h'-'a'] - number[8];
         number[5] = characters['f'-'a'] - number[4];
         number[7] = characters['s'-'a'] - number[6];
         number[9] = characters['i'-'a'] - number[6] - number[8] - number[5];

         StringBuilder result = new StringBuilder();

         for (int i = 0; i < number.length; i++) {
            while (number[i]-- > 0) {
                result.append(i);
            }
         }

         return result.toString();
    }
}
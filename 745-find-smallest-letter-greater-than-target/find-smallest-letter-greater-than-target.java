class Solution {
    // letters = ["c","f","j"], target = "a"
    // letters = ["c","f","j"], target = "c"
    // letters = ["x","x","y","y"], target = "z"
    // time: O(n) 
    // space: O(1)
    public char nextGreatestLetter(char[] letters, char target) {
        for (char c : letters) {
            if (Character.compare(c, target) > 0) {
                return c;
            }
        }
        return letters[0];
    }
}
class Solution {
    // Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
    // Output: true
    // stack = []
    // 
    // stack.push(pushed[i])
    // 

    // Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
    // Output: false
    // 
    public boolean validateStackSequences(int[] pushed, int[] popped) {
        Stack<Integer> stack = new Stack<>();
        int i = 0;

        for (int num : pushed) {
            stack.push(num);
            while(!stack.isEmpty() && stack.peek() == popped[i]) {
                stack.pop();
                i++;
            }
        }

        return stack.isEmpty();
    }
}
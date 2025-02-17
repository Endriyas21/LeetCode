class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        int[] res = new int[n];
        Stack<Integer> stack = new Stack<>();

        for (int i =0; i< n; i++){
            while (!stack.isEmpty() && temperatures[stack.peek()] < temperatures[i]){
                int index = stack.pop();
                res[index] = i - index;
                 
                
            }
            stack.push(i);
        }
        return res;   

    }
}
class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> store = new HashMap<>();
        store.put(')', '(');
        store.put('}', '{');
        store.put(']', '[');
        Stack<Character> stack = new Stack<>();

        for (char ch : s.toCharArray()) {
            if (store.containsKey(ch)) {
                if (!stack.isEmpty() && stack.peek() == store.get(ch)) {
                    stack.pop();
                } else {
                    return false;
                }
            } else {
                stack.push(ch);
            }
        }
        return stack.isEmpty();
    }
}
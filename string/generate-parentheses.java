class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        dfs(res, new StringBuilder(), 0, 0, n);
        return res;        
    }

    private void dfs(List<String> res, StringBuilder current, int open, int close, int max ){
        if (open == max && close == max){
            res.add(current.toString());
            return;
        }
        if (open < max){
            current.append('(');
            dfs(res, current, open+1, close, max);
            current.deleteCharAt(current.length() -1);
        }
        if (close < open){
            current.append(')');
            dfs(res, current, open, close+1, max);
            current.deleteCharAt(current.length() -1);
        }
    }
}
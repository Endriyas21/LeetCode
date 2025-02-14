class Solution {
    public boolean isValidSudoku(char[][] board) {
        Map<Integer, Set<Character>> rows = new HashMap<>();
        Map<Integer, Set<Character>> cols = new HashMap<>();
        Map<Integer, Set<Character>> square = new HashMap<>();

        for (int i =0; i <= 9; i++){
            rows.put(i, new HashSet<>());
            cols.put(i, new HashSet<>());
            square.put(i, new HashSet<>());

        }

        for (int i =0; i<=9; i++){
            for (int j =0; j<=9; j++){
                char w = board[i][j];
                
                if (w == "."){
                    continue;
                }
                int index = (i/3)*3 + (j/3);
                if (rows.get(i).contain(w) || cols.get(j).contains(w) || square.get(index).contains(w)){
                    return False;
                }
                rows.get(i).add(w);
                cols.get(j).add(w);
                square.get(index).add(w);

            }
        }
        return True;
    }
}
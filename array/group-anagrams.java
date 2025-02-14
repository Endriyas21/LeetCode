class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> store = new HashMap<>();
        for (String str: strs){
            char[] key = str.toCharArray();
            Arrays.sort(key);
            String new_key = new String(key);
            if (!store.containsKey(new_key)){
                store.put(new_key, new ArrayList<>());
            } 
            store.get(new_key).add(str);
        }
        return new ArrayList<>(store.values());
    }
}
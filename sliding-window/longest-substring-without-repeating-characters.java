class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> store = new HashSet<>();
        int maxLen = 0;
        int l =0;
        for (int r=0; r < s.length(); r++){
            while (store.contains(s.charAt(r))){
                store.remove(s.charAt(l));
                l+=1;
            }
            store.add(s.charAt(r));
            maxLen = Math.max(maxLen, r -l+1);

        }
        return maxLen;
        }
        
    }

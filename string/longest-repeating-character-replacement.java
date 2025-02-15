class Solution {
    public int characterReplacement(String s, int k) {
        Map<Character, Integer> store = new HashMap<>();
        int maxLen = 0;
        int l = 0;
        int maxCount = 0;

        for (int r = 0; r < s.length(); r++) {
            char currentChar = s.charAt(r);
            store.put(currentChar, store.getOrDefault(currentChar, 0) + 1);
            maxCount = Math.max(maxCount, store.get(currentChar));

            while ((r - l + 1) - maxCount > k) {
                char leftChar = s.charAt(l);
                store.put(leftChar, store.get(leftChar) - 1);
                l += 1;
            }

            maxLen = Math.max(maxLen, r - l + 1);
        }

        return maxLen;
    }
}
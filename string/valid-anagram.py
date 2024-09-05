class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        store_s, store_t= {}, {}
        for i in range(len(s)):
            store_s[s[i]] = 1 + store_s.get(s[i],0)
            store_t[t[i]] = 1 + store_t.get(t[i],0)
        return store_s == store_t
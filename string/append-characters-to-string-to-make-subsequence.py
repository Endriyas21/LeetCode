class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        r,l = 0,0
        while r < len(s) and l < len(t):
            if t[l] == s[r]:
                l+=1
            r+=1
        return len(t) - l   
            
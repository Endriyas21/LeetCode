class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res,l = 0,0
        for r in range(len(s)):
            count[s[i]] = 1 + count.get(s[i],0)
            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -=1
                l+=1

        return res

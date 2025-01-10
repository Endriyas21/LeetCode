class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res,l = 0, 0
        count = set()
        for r in range(len(s)):
            if s[r] not in count:
                count.add(s[r])
                res = max(r-l+1, res)
            else:
                while l < r and s[r] in count:
                    count.remove(s[l])
                    l+=1
                count.add(s[r]) #be aware
        return res
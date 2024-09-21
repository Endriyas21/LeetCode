class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        need, have = len(t), 0
        res, reslen = [-1,-1], float('inf')
        window, count_t = Counter(), Counter(t)
        l = 0
        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char, 0)
            if char in t and count_t[char] == window[char]:
                have+=1
            while need == have:
                if (r -l+1) < reslen:
                    reslen = r-l+1
                    res = [l, r]
                window[s[l]] -=1
                if s[l] in t and count_t[s[l]] > window[s[l]]:
                    have -=1
                l+=1
        l, r = res
        return "" if res == float('inf') else s[l:r+1]
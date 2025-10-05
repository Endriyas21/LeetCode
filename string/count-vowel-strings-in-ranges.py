class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel = set("aeiou")
        prefix = [0]*(len(words)+1)
        res = []

        for i, w in enumerate(words):
            count = 0
            if w[0] in vowel and w[-1] in vowel:
                count+=1
            prefix[i+1] = count + prefix[i]

        for i,w in enumerate(queries):
            l,r = w
            res.append(prefix[r+1] - prefix[l])
        return res
            

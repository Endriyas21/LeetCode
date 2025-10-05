class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        def is_vowel_string(word):
            vowels = {"a", "e", "i", "o", "u"}
            return word[0] in vowels and word[-1] in vowels

        ans = []
        for l, r in queries:
            count = 0
            for word in words[l:r+1]:
                if is_vowel_string(word):
                    count += 1
            ans.append(count)
        return ans

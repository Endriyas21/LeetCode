class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1,len_s2 = len(s1), len(s2)

        s1_count = Counter(s1)
        window = Counter(s2[:len_s1])

        if window == s1_count:
            return True
        
        for i in range(len_s1, len_s2):
            window[s2[i]] +=1

            window[s2[i - len_s1]] -=1

            if window[s2[i - len_s1]] == 0:
                del window[s2[i - len_s1]]
            if window == s1_count:
                return True
        return False


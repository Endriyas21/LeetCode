class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l1 > l2:
            return False
        s1_count = Counter(s1)
        window = Counter(s2[:l1])
        if window == s1_count:
            return True
        for i in range(l1, l2):
            window[s2[i]] +=1
            window[s2[i-l1]] -=1

            if window[s2[i-l1]] == 0:
                del window[s2[i-l1]]
            if window == s1_count:
                return True
        return False

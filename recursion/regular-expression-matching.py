class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Create a DP table with (len(s)+1) rows and (len(p)+1) columns
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        # Base case: empty string matches empty pattern
        dp[len(s)][len(p)] = True

        # Fill the table backwards
        for i in range(len(s), -1, -1):  # i is index in s
            for j in range(len(p) -1, -1, -1):  # j is index in p
                # Check if current characters match
                first_match = (i < len(s)) and (p[j] == s[i] or p[j] == ".")
                # If next char in pattern is '*'
                if (j + 1 < len(p)) and (p[j + 1] == "*"):
                    # Two choices:
                    # 1. Skip the preceding element and '*'
                    # 2. If current matches, move to next char in s
                    dp[i][j] = dp[i][j + 2] or (first_match and dp[i + 1][j])
                else:
                    # No '*', just check current match and move both pointers
                    dp[i][j] = first_match and dp[i + 1][j + 1]
        # The answer is whether the whole string matches the whole pattern
        return dp[0][0]
        
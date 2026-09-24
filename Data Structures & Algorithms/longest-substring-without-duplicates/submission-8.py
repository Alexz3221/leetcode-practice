class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tip = 0
        max_len = 0
        seen = {}

        for tail in range(len(s)):
            if s[tail] in seen:
                tip = max(tip, seen[s[tail]] + 1)

            seen[s[tail]] = tail

            max_len = max(max_len, tail - tip + 1)

        return max_len
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        max_len = 0
        seen = set()
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])

            length = abs(l - r) + 1
            if length > max_len:
                max_len = length
            r += 1
        return max_len
            
            




        
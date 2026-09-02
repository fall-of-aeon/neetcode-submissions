from collections import Counter 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set = Counter(s)
        t_set = Counter(t)
        
        if len(s) != len(t):
            return False
        
        return s_set == t_set

        
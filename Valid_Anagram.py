class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        for c in s:
            t = t.replace(c, "", 1)
        return t == "" 
class Solution:
    def isValid(self, s: str) -> bool:
        valid = {'(': ')', '[': ']', '{': '}'}
        l = []

        for c in s:
            if c in valid.keys():
                l.insert(0, valid[c])
            else:
                if len(l) == 0 or l.pop(0) != c:
                    return False
        return len(l) == 0
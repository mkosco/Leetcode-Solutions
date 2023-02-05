class Solution:
    def isValid(self, s: str) -> bool:
        valid = {'(': ')', '[': ']', '{': '}'}
        indices = [x * 2 for x in range(len(s) // 2)]

        for i in indices:
            currentP = s[i]
            nextP = s[i+1]
            if nextP != valid[currentP]:
                return False
        return True


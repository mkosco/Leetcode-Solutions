class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        clean = ""

        # cleanup the input
        for c in s:
            if c.isalnum():
                clean += c
        
        #check for palindrom
        for i in range(len(clean)//2):
            left = i
            right = len(clean) - 1 - i
            if clean[left] != clean[right]:
                return False
            left += 1
            right -= 1
        return True
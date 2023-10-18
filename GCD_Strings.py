class Solution(object):
    def gcd(self, a, b):
        if a % b == 0:
            return b
        return self.gcd(b, a % b)

    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        gcd = self.gcd(len(str1), len(str2))
        gcd_str = str1[:gcd]

        # test the strings
        test_str1 = ''
        for i in range(len(str1)/gcd):
            test_str1 = test_str1 + gcd_str
        if test_str1 != str1:
            return ''

        test_str2 = ''
        for i in range(len(str2) / gcd):
            test_str2 = test_str2 + gcd_str
        if test_str2 != str2:
            return ''

        return gcd_str

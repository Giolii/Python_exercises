# Last updated: 8/13/2025, 5:10:24 PM
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ""

        def gcd(len1,len2):
            while len2:
                len1,len2 = len2, len1%len2
            return len1
            # min_str = min(len1,len2)

            # for i in range(min_str,0,-1):
            #     if len1 % i == 0 and len2 % i == 0:
            #         return i
            # return 1
        return str1[:gcd(len(str1),len(str2))]


# Last updated: 8/13/2025, 5:10:09 PM
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # result = []
        # for a,b in zip(word1,word2):
        #     result.append(a+b)
        # result.append(word1[len(word2):])
        # result.append(word2[len(word1):])
        # return "".join(result)
        
        result = ''
        p1,p2 = 0,0

        while p1 < len(word1) or p2 < len(word2):
            if p1 < len(word1):
                result += word1[p1]
                p1 += 1
            if p2 < len(word2):
                result += word2[p2]
                p2 += 1
        return result
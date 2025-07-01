# Last updated: 7/1/2025, 4:19:08 PM
class Solution:
    def dfs(self,n,k,rootVal):
        if n == 1:
            return rootVal
        
        totalNodes = 2**(n-1)
        
        if k > (totalNodes / 2):
            nextRootVal = 1 if rootVal == 0 else 0
            return self.dfs(n -1, k - (totalNodes / 2), nextRootVal)
        else:
            nextRootVal = 0 if rootVal == 0 else 1
            return self.dfs(n -1, k,nextRootVal)
    
    def kthGrammar(self,n,k):
        return self.dfs(n,k,0)
            
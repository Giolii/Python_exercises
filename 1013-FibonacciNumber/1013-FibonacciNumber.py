# Last updated: 6/30/2025, 4:59:43 PM
class Solution:
    def fib(self, n: int) -> int:
        cache = {}

        def fib_rec(n):
            if n < 2:
                return n
            
            if n in cache:
                return cache[n]
            
            result = self.fib(n-1) + self.fib(n-2)
            cache[n] = result
            return result
        return fib_rec(n)
# Last updated: 6/25/2025, 11:43:37 AM
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        i,j = len(a) -1, len(b) -1
        
        while i >= 0 or j >= 0 or carry:
            bit_a = int(a[i]) if i>=0 else 0
            bit_b = int(b[j]) if j>= 0 else 0
            
            total = bit_a + bit_b + carry
            result.append(str(total % 2))
            carry = total // 2
            
            i-=1
            j-=1
        return ''.join(reversed(result))
            
        
# Last updated: 7/9/2025, 6:29:58 PM
class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        results = [0] * len(temps)
        stack = []
        
        for i,temp in enumerate(temps):
            while stack and temps[stack[-1]] < temp:
                index = stack.pop()
                results[index] = i - index
            stack.append(i)
        return results
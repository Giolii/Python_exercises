# Last updated: 7/7/2025, 4:14:31 PM
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        
        if "0000" in deadends:
            return -1
        
        queue = deque([('0000',0)])
        visited = set('0000')
        
        while queue:
            current,moves = queue.popleft()
            
            if current == target:
                return moves 
            
            for i in range(4):
                for delta in [-1,1]:
                    new_digit = (int(current[i])+delta)%10
                    new_combination = (current[:i] + str(new_digit) + current[i+1:])
                    if new_combination not in visited and new_combination not in deadends:
                        visited.add(new_combination)
                        queue.append((new_combination,moves + 1))
        return -1
        
        
        
        
#         deadends = set(deadends)
        
#         if "0000" in deadends:
#             return -1
        
#         queue = deque([('0000',0)])
#         visited = set('0000')
        
#         while queue:
#             current_combination,moves = queue.popleft()
            
#             if current_combination == target:
#                 return moves
            
#             for i in range(4):
#                 for delta in [-1,1]:
#                     new_digit = (int(current_combination[i]) + delta) % 10
#                     new_combination = (
#                         current_combination[:i] + str(new_digit) + current_combination[i+1:]
#                     )
                    
#                     if new_combination not in visited and new_combination not in deadends:
#                         visited.add(new_combination)
#                         queue.append((new_combination, moves + 1))
#         return -1
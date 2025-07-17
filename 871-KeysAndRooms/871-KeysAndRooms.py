# Last updated: 7/16/2025, 6:14:03 PM
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
#         BFS
        n = len(rooms)
        visited = set([0])
        queue = deque([0])
        
        while queue:
            room = queue.popleft()
            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    queue.append(key)
        return len(visited) == n        
        
        
        
        
#           DFS        
#         n = len(rooms)
#         seen=set()
        
#         def dfs(room):
#             if room in seen:
#                 return
#             seen.add(room)
            
#             for key in rooms[room]:
#                 dfs(key)
#         dfs(0)
#         return len(seen) == n
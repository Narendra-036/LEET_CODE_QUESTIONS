class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        def dfs(node, parent):
            
            res = 0
            if node not in visited:
                visited.add(node)
                
                for nei in adj_list[node]:
                    if nei != parent: 
                        
                        children_time = dfs(nei, node) 

                        if children_time > 0 or hasApple[nei]:
                        
                            res += children_time + 2
                    
            return res
            
        adj_list = defaultdict(list)
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        # print(adj_list)
        
        visited = set()
        return dfs(0, None)
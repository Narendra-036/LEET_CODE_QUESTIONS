class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n==1:
            return True
        adj_mat=[[] for _ in range(n)]
        for i in edges:
            adj_mat[i[0]].append(i[1])
            adj_mat[i[1]].append(i[0])
        print(adj_mat)
        check=[False for _ in range(n)]
        check[source]=True
        x=adj_mat[source]
        for i  in x:
            check[i]=True
            if i==destination:
                return True
        while x:
            y=x.pop(-1)
            for i in adj_mat[y]:
                if not check[i]:
                    x.append(i)
                    check[i]=True
                if i==destination:
                    return True
        return False
            
            
            
class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        ans=0
        s=0
        x=0
        for i in logs:
            y=i[1]-x
            if ans<=y:
                if ans==y:
                    s=min(s,i[0])
                else:
                    s=i[0]
                ans=y
                
            x=i[1]
        return s
            
            
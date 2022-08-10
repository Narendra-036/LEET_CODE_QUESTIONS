class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_dist=99999
        idx=-1
        for i,cord in enumerate(points):
            dist=abs(cord[0]-x)+abs(cord[1]-y)
            if (x==cord[0] or y==cord[1]) and dist<min_dist:
                min_dist=dist
                idx=i
        return idx
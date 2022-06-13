class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        a=[]
        for i in range(len(rectangles)):
            a.append(min(rectangles[i]))
        count=0
        m=max(a)
        for i in range(len(a)):
            if m==a[i]:
                count+=1
        return count
class Solution:
    def divide(self, x: int, y: int) -> int:
        result=0
        minus=False
        if x<0 or y<0 :
            minus=True
        if x<0 and y<0:
            minus=False
        
        x=abs(x)
        y=abs(y)
        
#         while x<10000000000*y:
#             x-=10000000000*y
#             result+=10000000000
        
        
#         while x<1000000*y:
#             x-=1000000*y
#             result+=1000000
        
        
#         while x<1000*y:
#             x-=1000*y
#             result+=1000
        
#         while x<100*y:
#             x-=100*y
#             result+=100
        
        
#         while x<=y:
#             x-=y
#             result+=1
        
        
#         if minus:
#             result*=-1
        
        result=x//y
        if minus:
            result*=-1
        
        
        if result>pow(2,31)-1:
            result= pow(2,31)-1
        if result<-pow(2,31):
            result=-pow(2,31)
        
        
        return result
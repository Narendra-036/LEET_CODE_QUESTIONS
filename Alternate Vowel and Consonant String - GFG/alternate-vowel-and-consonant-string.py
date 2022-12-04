#User function Template for python3

class Solution:
    def rearrange(self, S, N):
        # code here
        x=['a','e','i','o','u']
        o=[]
        c=[]
        for i in S:
            if i in x:
                o.append(i)
            else:
                c.append(i)
        if abs(len(c)-len(o))>1:
            return -1
        else:
            a,b=0,0
            o.sort()
            c.sort()
            if len(c)>len(o):
                a,b=len(c),len(o)
            else:
                a,b=len(o),len(c)
            ans=""
            if a==len(o):
                i=0
                while len(ans)<N:
                    ans+=o[i]
                    if len(c)>i:
                        ans+=c[i]
                    i+=1
            if a==len(c):
                i=0
                while len(ans)<N:
                    ans+=c[i]
                    if len(o)>i:
                        ans+=o[i]
                    i+=1
            return ans
                
                    
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N = int(input().strip())
        S = input().strip()
        ob=Solution()
        ans=ob.rearrange(S, N)
        print(ans)
# } Driver Code Ends
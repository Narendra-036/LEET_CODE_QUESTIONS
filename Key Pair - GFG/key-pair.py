#User function Template for python3
class Solution:
	def hasArrayTwoCandidates(self,arr, n, x):
	    
	    d={}
	    for i in arr:
	        if i not in d:
	            d[x-i]=1
	        else:
	            return 1
	    return 0
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.hasArrayTwoCandidates(arr, n, x)
        if ans:
            print("Yes")
        else:
            print("No")
        tc -= 1

# } Driver Code Ends
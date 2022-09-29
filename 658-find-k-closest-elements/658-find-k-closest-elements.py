class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        d={}
        for i,num in enumerate(arr):
            if abs(num-x) in d:
                d[abs(num-x)].append(num)
            else:

                d[abs(num-x)]=[]
                d[abs(num-x)].append(num)
        ans=[]
        for i in sorted(d.keys()):
            if len(ans)>=k:
                break
            ans.extend(d[i])
        ans=ans[:k]
        ans.sort()
        return ans
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        x=strs[0]
        ans=""
        # if len(strs)==1:
        #     return strs[-1]
        for i in range(1,len(x)+1):
            count=0
            for j in strs:
                if x[:i] in j[:i]:
                    count+=1
                
            if count==len(strs):
                ans=x[:i]
        return ans
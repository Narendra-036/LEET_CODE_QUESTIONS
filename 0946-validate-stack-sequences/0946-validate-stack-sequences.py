class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        x=[]
        while popped or pushed:
            
                
            if len(pushed)>0:
                x.append(pushed[0])
                l=pushed.pop(0)
            
            while  len(x)>0 and x[-1]==popped[0]:
                x.pop(-1)
                popped.pop(0)
            if   len(pushed)==0 and len(x)>0 and x[-1]!=popped[0]:
                return False
            
        return True
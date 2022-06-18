class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        a=[0]
        a.append(gain[0])
        for i in range(1,len(gain)):
            gain[i]=max(gain[i],gain[i-1])+min(gain[i],gain[i-1])
            a.append(gain[i])
            
        print(a)
        return max(a)
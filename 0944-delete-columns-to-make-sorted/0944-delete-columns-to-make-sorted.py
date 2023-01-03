class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(list(col) != sorted(col) for col in zip(*strs))
        # count=0
        # for i in strs:
        #     x=[j for j in i]
        #     # print(x)
        #     y=x[:]
        #     y.sort()
        #     if x==y[::-1] or x==y:
        #         continue
        #     else:
        #         count+=1
        # return count
                
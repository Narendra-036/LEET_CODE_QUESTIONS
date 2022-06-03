class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        q=[]
        for i in image:
            
            q.append(list(map(lambda x: 0 if x == 1 else 1, i[::-1])))
        return q
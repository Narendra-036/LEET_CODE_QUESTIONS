class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        r=len(image)
        c=len(image[0])
        x=image[sr][sc]
        arr=[[sr,sc]]
        i=0
        while i<len(arr):
            R=arr[i][0]
            C=arr[i][1]
            image[R][C]=color
            if C-1>=0 and [R,C-1] not in arr and image[R][C-1]==x:
                arr.append([R,C-1])
            if C+1<len(image[0]) and [R,C+1] not in arr and image[R][C+1]==x:
                arr.append([R,C+1])
            if R-1>=0 and [R-1,C] not in arr and image[R-1][C]==x:
                arr.append([R-1,C])
            if R+1<len(image) and [R+1,C] not in arr and image[R+1][C]==x:
                arr.append([R+1,C])
            i+=1
        return image
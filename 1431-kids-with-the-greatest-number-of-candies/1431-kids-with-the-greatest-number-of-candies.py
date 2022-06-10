class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        a=[False]*len(candies)
        x=max(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies>=x:
                a[i]=True
        return a
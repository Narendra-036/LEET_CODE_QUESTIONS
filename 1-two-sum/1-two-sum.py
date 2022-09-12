class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        for i in range(len(arr)):
            x=target-arr[i] 
            if x in arr:
                for j in range(len(arr)):
                    if x==arr[j] and j!=i:
                        return [i,j]
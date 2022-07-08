class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        curr_layer, next_layer = set([(-1, -1)]), set()
        i3 = 0
        
        while curr_layer and i3 < len(s3):
            for i1, i2 in curr_layer:
                if i1 + 1 < len(s1) and s1[i1 + 1] == s3[i3]:
                    next_layer.add((i1 + 1, i2))
                if i2 + 1 < len(s2) and s2[i2 + 1] == s3[i3]:
                    next_layer.add((i1, i2 + 1))
            curr_layer, next_layer = next_layer, set()
            if curr_layer:
                i3 += 1
        
        return i3 == len(s3)
class Solution:
    def compress(self, chars: List[str]) -> int:
        p=chars[0]
        count=0
        j=0
        for i in chars:
            if p==i:
                count+=1
            if p!=i:
                chars[j]=p
                j+=1
                if count>1:
                    for k in str(count):
                        chars[j]=str(k)
                        j+=1
                p=i
                count=1
        chars[j]=p
        j+=1
        if count>1:
            for i in str(count):
                chars[j]=i
                j+=1
        return j

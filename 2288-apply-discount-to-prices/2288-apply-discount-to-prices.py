class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        l = sentence.split(' ')
        for i in range(len(l)):
            if (len(l[i]) > 1) and (l[i][0] == '$') and (l[i][1:].isdigit()):
                l[i] = '$' + '%.2f'%((100-discount)/100 * int(l[i][1:]))
        return ' '.join(l)
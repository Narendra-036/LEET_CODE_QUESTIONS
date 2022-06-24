class Solution:
    def isPossible(self, target: List[int]) -> bool:
        n = len(target)
        curr_sum = sum(target)
        
        heap = [-num for num in target]
        heapq.heapify(heap)
        
        while heap[0] != -1:
            num = -heapq.heappop(heap)
            curr_sum -= num
            if curr_sum == 1:
                return True
            if curr_sum >= num or curr_sum == 0 or num % curr_sum == 0:
                return False
            num %= curr_sum
            curr_sum += num
            heapq.heappush(heap, -num)
            
        return True
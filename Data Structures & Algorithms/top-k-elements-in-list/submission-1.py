import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums :
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        heap = []
        for key,val in freq.items():
            if len(heap) < k or val > heap[0][0]:
                heapq.heappush(heap,[val,key])
            if len(heap) > k:
                heapq.heappop(heap)
        return[i[1] for i in heap]
        
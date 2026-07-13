class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heapq.heapify_max(gifts)
        for _ in range(k):
            element = heapq.heappop_max(gifts)
            element = (element ** 0.5) // 1
            heapq.heappush_max(gifts, element)
        return int(sum(gifts))
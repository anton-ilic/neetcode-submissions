class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # distance, index
        distances = []
        for i in range(0, len(points)):
            distance = points[i][0] ** 2 + points[i][1] ** 2
            heapq.heappush(distances, (distance, i))
        
        ans = []
        for _ in range(k):
            idx = heapq.heappop(distances)[1]
            ans.append(points[idx])
        return ans
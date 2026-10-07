class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        k
        for point in points:
            x, y = point
            distance = x**2 + y**2
  
            heapq.heappush(heap, (-distance, point))
            if len(heap) > k: heapq.heappop(heap)
        answer = []
  
        for _ in range(k):
            distance, point = heapq.heappop(heap)
            answer.append(point)
        return answer
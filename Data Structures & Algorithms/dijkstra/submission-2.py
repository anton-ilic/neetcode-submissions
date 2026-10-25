class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # Djsktra's: expand the shortest path
        fringe = [] # min heap; [cost from SRC, element]
        costs = {}

        for edge in edges:
            if edge[0] == src:
                heapq.heappush(fringe, (edge[2], edge[1]))
            # costs[edge[0]] = -1
            # costs[edge[1]] = -1
        for i in range(n):
            costs[i] = -1
        costs[src] = 0 # self is 0


        while len(fringe) != 0:
            element = heapq.heappop(fringe)

            # already reached this with shorter path
            if costs.get(element[1], -1) != -1:
            # if element[1] in costs:
                continue

            costs[element[1]] = element[0]
            # now that we've established the cost, check its neighbors
            src = element[1]
            for edge in edges:
                if edge[0] == src:
                    heapq.heappush(fringe, (edge[2] + element[0], edge[1]))
        
        # ADD non-reached edges as -1

        return costs
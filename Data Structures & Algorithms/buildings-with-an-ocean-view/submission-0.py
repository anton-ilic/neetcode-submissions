class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        # right to left
        buildings = deque()
        for i in range(len(heights) - 1, -1, -1):
            if len(buildings) == 0 or heights[buildings[0]] < heights[i]:
                buildings.appendleft(i)
        return list(buildings)
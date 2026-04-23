class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen = set()
        current_x = 0
        current_y = 0
        seen.add(str(current_x) + ":" + str(current_y))
        for d in path:
            
            if d == "N":
                current_y += 1
            elif d == "E":
                current_x += 1
            elif d == "S":
                current_y -= 1
            elif d == "W":
                current_x -= 1
            curr = str(current_x) + ":" + str(current_y)
            if curr in seen:
                return True
            seen.add(curr)
            
            

        return False
            
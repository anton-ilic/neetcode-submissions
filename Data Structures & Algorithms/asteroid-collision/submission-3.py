class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []

        for asteroid in asteroids:
            if len(ans) != 0 and ans[-1] > 0 and asteroid < 0:
                # right moving ans, left moving asteroid

                # shouldnt ans[-1] > 0 handle the case where its -2, -2, 1, -2
                while len(ans) != 0 and ans[-1] > 0:
                    if abs(asteroid) == abs(ans[-1]):
                        ans.pop()
                        asteroid = 0
                        break
                    elif abs(asteroid) > abs(ans[-1]):
                        # asteroid is bigger
                        ans.pop()
                        
                    else:
                        # asteroid is smaller
                        break
                
                if (asteroid != 0) and (len(ans) == 0 or ans[-1] < 0):
                    ans.append(asteroid)

            else:
                ans.append(asteroid)


        return ans
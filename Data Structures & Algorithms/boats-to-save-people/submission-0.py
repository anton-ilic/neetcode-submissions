class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # O(n) ** 2 ==> for each start, find end that's less then weight limit? 

        total = 0
        people.sort()

        low = 0
        high = len(people) - 1
        while low <= high:
            if people[low] + people[high] > limit:
                total += 1
                high -= 1
                continue
            total += 1
            low += 1
            high -= 1
        return total
class Solution:
    def solves_problem(self, weights, days, w):
        weights_copy = weights.copy()
        current_days = days
        remaining_w = w
        while len(weights_copy) != 0 and current_days > 0:
            current_weight = weights_copy[0]
            if current_weight > remaining_w:
                remaining_w = w
                current_days -= 1
            else:
                remaining_w -= current_weight
                weights_copy.pop(0)
        return len(weights_copy) == 0
 

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #It is not allowed to load weight more than the maximum weight capacity of the ship.

        # almost like a binary search problem?
        low = max(weights)
        high = sum(weights)
        while low < high:
            mid = low + (high - low) // 2
            if self.solves_problem(weights, days, mid):
                high = mid
            else:
                low = mid + 1
        return low 
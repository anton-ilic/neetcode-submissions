class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        total = 0
        for i in range(0, len(customers)):
            if grumpy[i] == 0:
                total += customers[i]
        
        # baseline total
        current = total

        # if minutes < len(customers) ==> return all customers
        if minutes >= len(customers):
            return sum(customers)

        for i in range(0, minutes):
            if grumpy[i] == 1:
                current += customers[i]

        for i in range(minutes, len(customers)):
            # how much better is the total if we start at this candidate
            
            # add current if is grumpy, remove current - minutes IF is grumpy
            total = max(total, current)
            
            if grumpy[i] == 1:
                current += customers[i]

            if grumpy[i - minutes] == 1:
                current -= customers[i - minutes]
            
            
            
        return max(total, current)
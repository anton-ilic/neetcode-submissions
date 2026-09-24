class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # everyone in front to buy min(tickets[k], tickets[i]), everyone behind buys  min(tickets[k] - 1, tickets[i])
        tickets_k = tickets[k]
        total = 0
        for i in range(0, len(tickets)):
            if i <= k:
                total += min(tickets[k], tickets[i])
            else:
                total += min(tickets[k] - 1, tickets[i])
        return total
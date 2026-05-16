class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # ok so btwn 2 even numbers
        # 2 to 4 ==> 3 --> 1
        # 2 to 6 ==> 3, 4, 5 --> 2
        # 2 to 8 ===> 3, 4, 5, 6, 7 -- > 3

        # ok so difference // 2 

        # 2 to 3 --> 1 (3)
        # 2 to 5 --> 3, 5 --> 5 - 2 
        #3, 5 
        if low % 2 == 0 and high % 2 == 0:
            return (high - low) // 2
        elif low % 2 == 0 or high % 2 == 0:
            return (high - low + 1) // 2
        else:
            return (high - low) // 2 + 1
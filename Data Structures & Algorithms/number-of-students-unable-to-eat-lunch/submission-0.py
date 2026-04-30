class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # bruteforce: simulate it
        # zeros = 0
        # for sandwhich in sandwiches:
        #     if sandwhich == 0:
        #         zeros += 1
        # ones = len(sandwiches) - zeros

        zeros_needed = 0
        ones_needed = 0
        for student in students:
            if student == 0:
                zeros_needed += 1
            else:
                ones_needed += 1
        
        for sandwhich in sandwiches:
            if sandwhich == 0:
                if zeros_needed != 0:
                    zeros_needed -= 1
                else:
                    return ones_needed
            else:
                if ones_needed != 0:
                    ones_needed -= 1
                else:
                    return zeros_needed
        return ones_needed + zeros_needed
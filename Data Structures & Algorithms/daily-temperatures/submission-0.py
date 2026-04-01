class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # maybe a stack of temperatures, index
        sol = [0] * len(temperatures)
        temp_stck = []
        ind_stck = []
        for i in range(len(temperatures) - 1, -1, -1):
            while len(temp_stck) != 0:
                current_temp = temp_stck.pop()
                current_ind = ind_stck.pop()
                if current_temp > temperatures[i]:
                    temp_stck.append(current_temp)
                    ind_stck.append(current_ind)
                    temp_stck.append(temperatures[i])
                    ind_stck.append(i)
                    sol[i] = abs(i - current_ind)
                    break

            if len(temp_stck) == 0:
                sol[i] = 0
                temp_stck.append(temperatures[i])
                ind_stck.append(i)
        return sol

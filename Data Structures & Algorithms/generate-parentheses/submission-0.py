class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []


        def generate(n, current_open, current_closed, current):
            if n == current_open and n == current_closed:
                ans.append(current)
                return 

            if current_closed > current_open:
                return

            if current_open < n:
                generate(n, current_open + 1, current_closed, current + "(")
                
            if current_closed < n:
                generate(n, current_open, current_closed + 1, current + ")")
        generate(n, 0, 0, "")
        return ans
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack for elements
        seen = []
        for element in tokens:
            if element == "+":
                seen.append(seen.pop() + seen.pop())
            elif element == "-":
                seen.append(-1 * seen.pop() + seen.pop())
            elif element == "*":
                seen.append(seen.pop() * seen.pop())
            elif element == "/":
                a = seen.pop()
                seen.append(int(seen.pop() / a))
            else:
                seen.append(int(element))
        return int(seen[0])
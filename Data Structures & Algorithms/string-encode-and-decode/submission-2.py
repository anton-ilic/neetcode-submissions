class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = []
        for s in strs:
            ans.append(str(len(s)) + "#" + s)
        return ''.join(ans)

    def decode(self, s: str) -> List[str]:
        index = 0
        ans = []
        
        start = 0
        while index < len(s):
            start = index
            current = 0
            while s[index].isdigit():
                current = current * 10 + int(s[index])
                index += 1

            if s[index] == '#':
                ans.append(s[index + 1 : index + 1 + current])
            index = index + current + 1

        return ans
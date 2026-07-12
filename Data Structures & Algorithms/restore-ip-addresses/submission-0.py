class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        permutations = []

        def permute_address(i, current, parts):
            if i == len(s) and parts == 4:
                
                permutations.append(current[1:])
                return 
            elif i >= len(s):
                return
            
            permute_address(i + 1, current + "." + s[i], parts + 1)

            if s[i] == "0":
                return
            
            permute_address(i + 2, current + "." + s[i: i + 2], parts + 1)

            if int(s[i : i + 3]) > 255:
                return

            permute_address(i + 3, current + "." + s[i: i + 3], parts + 1)
        permute_address(0, "", 0)
        return permutations
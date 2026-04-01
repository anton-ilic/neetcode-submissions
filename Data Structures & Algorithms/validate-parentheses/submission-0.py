class Solution:
    def isValid(self, s: str) -> bool:
        stck = []
        for bracket in s:
            if bracket == "[" or bracket == "(" or bracket == "{":
                stck.append(bracket)
            else:
                try:
                    opener = stck.pop()
                    if opener == "[" and bracket == "]" or opener == "(" and bracket == ")" or opener == "{" and bracket == "}":
                        continue
                    return False
                except:
                    return False
        return len(stck) == 0
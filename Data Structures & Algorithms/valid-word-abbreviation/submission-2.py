class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        current = 0
        end = len(word)

        current_number = 0
        for i in range(0, len(abbr)):
            if current_number != 0 and abbr[i].isdigit():
                current_number = current_number * 10 + int(abbr[i])
            elif abbr[i].isdigit():
                if abbr[i] == "0":
                    return False
                current_number = int(abbr[i])
            else:
                current = current + current_number
                if current >= end:
                    return False

                if word[current] != abbr[i]:
                    return False
                current += 1
                current_number = 0
            
        current = current + current_number
        return current == end
        


                
            
            

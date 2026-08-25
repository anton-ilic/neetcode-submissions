class Solution:
    def compress(self, chars: List[str]) -> int:
        # we don't need to actually append it; just keep a count
        count = 0

        current = chars[0]
        current_count = 1

        low = 0
        
        for i in range(1, len(chars)):
            if chars[i] == current:
                current_count += 1
            else:
                # add current character + len(str(current_count))
                count += 1 # current char
                chars[low] = current
                low += 1
                if current_count != 1:
                    current_count_str = str(current_count)
                    for j in range(0, len(str(current_count_str))):
                        chars[low] = current_count_str[j]
                        low += 1
                        count += 1
                current = chars[i]
                current_count = 1
        
        if current_count != 0:
            count += 1 # current char
            chars[low] = current
            low += 1
            if current_count != 1:
                current_count_str = str(current_count)
                for j in range(0, len(str(current_count_str))):
                    chars[low] = current_count_str[j]
                    low += 1
                    count += 1 
        return count
            

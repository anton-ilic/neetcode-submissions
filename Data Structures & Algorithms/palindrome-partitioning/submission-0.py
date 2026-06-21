class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        END = len(s)

        def split_remaining(s, current_palindromes, current_idx):
            # try splitting current_idx to end; then current_idx to end - 1... all the way to just current_idx
            if current_idx == END:
                ans.append(current_palindromes)
                return
            
            for potential_end in range(END, current_idx, -1):
                current_candidate = s[current_idx:potential_end]
                # if this is a palindrome, go thru from here
                if current_candidate == current_candidate[::-1]:
                    candidate_palindromes = current_palindromes.copy()
                    candidate_palindromes.append(current_candidate)
                    split_remaining(s, candidate_palindromes, potential_end)
            return 
        split_remaining(s, [], 0)
        return ans
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # sort folders by length asc 
        folder.sort(key = lambda x : len(x))

        seen = set()
        ans = []
        for f in folder:
            # if any subsection of the prefix is in seen; then don't add this part
            is_seen = False
            subsections = f.split('/')[1:]
            current = ""
            for subsection in subsections:
                current = current + "/" + subsection
                if current in seen:
                    is_seen = True
                    break


            if not is_seen:
                seen.add(f)
                ans.append(f)
        return ans
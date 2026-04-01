from typing import List

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        prereq_map = {}
        for pair in prerequisites:
            prereq = pair[0]
            course = pair[1]
            if course not in prereq_map:
                prereq_map[course] = []
            prereq_map[course].append(prereq)

        def has_prereq(target: int, course: int, seen: set) -> bool:
            if course not in prereq_map:
                return False

            for pre in prereq_map[course]:
                if pre == target:
                    return True
                if pre not in seen:
                    seen.add(pre)
                    if has_prereq(target, pre, seen):
                        return True

            return False

        ans = []
        for query in queries:
            prereq = query[0]
            course = query[1]
            ans.append(has_prereq(prereq, course, set()))

        return ans
class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        visited = set()
        path = set()

        def dfs(course):
            if course in path:
                return False

            if course in visited:
                return True

            path.add(course)

            for prereq in graph[course]:
                if not dfs(prereq):
                    return False

            path.remove(course)
            visited.add(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True

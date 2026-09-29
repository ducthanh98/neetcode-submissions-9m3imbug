class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        q = deque()
        adj = {i : [] for i in range(numCourses)}
        indegree =  [0] * numCourses

        for pre in prerequisites:
            a,b = pre
            adj[b].append(a)
            indegree[a] += 1 

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            key = q.popleft()
            next_courses = adj[key]

            for c in next_courses:
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.append(c)
        
        for v in indegree:
            if v > 0:
                return False
        return True

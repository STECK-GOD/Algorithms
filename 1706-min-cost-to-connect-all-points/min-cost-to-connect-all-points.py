class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        parent = [i for i in range(n)]
        
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i]) 
            return parent[i]
        
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j 
                return True
            return False
        
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))
        
        edges.sort()
        ans = 0
        count = 0
        
        for dist, i, j in edges:
            if union(i, j): 
                ans += dist
                count += 1
                if count == n - 1:
                    break
                    
        return ans
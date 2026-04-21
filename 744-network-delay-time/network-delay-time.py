import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # Представление графа в виде списка смежности
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        # Очередь с приоритетами: (время_до_узла, текущий_узел)
        pq = [(0, k)]
        # Хранение минимального времени прибытия для каждого узла
        shortest_paths = {}

        while pq:
            time, u = heapq.heappop(pq)
            if u in shortest_paths:
                continue
            shortest_paths[u] = time
            
            for v, w in adj[u]:
                if v not in shortest_paths:
                    heapq.heappush(pq, (time + w, v))

        # Возврат максимума из минимальных путей, если посещены все узлы
        return max(shortest_paths.values()) if len(shortest_paths) == n else -1
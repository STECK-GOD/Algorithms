class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        island_count = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            # Базовый случай: выход за границы или попадание на воду
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return
            
            # Пометка текущей клетки как обработанной
            grid[r][c] = '0'
            
            # Обход соседних клеток
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    island_count += 1
                    dfs(r, c) # Удаление обнаруженного острова из сетки

        return island_count
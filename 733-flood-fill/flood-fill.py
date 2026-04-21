class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_color = image[sr][sc]
        
        # Если цвет уже нужный, ничего не делаем, чтобы избежать бесконечной рекурсии
        if start_color == color:
            return image 

        def dfs(r, c):
            # Проверяем выходы за границы матрицы и совпадение цвета пикселя
            if 0 <= r < len(image) and 0 <= c < len(image[0]) and image[r][c] == start_color:
                image[r][c] = color  # Закрашиваем текущий пиксель
                
                # Идем рекурсивно в четыре стороны
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)

        dfs(sr, sc)
        return image
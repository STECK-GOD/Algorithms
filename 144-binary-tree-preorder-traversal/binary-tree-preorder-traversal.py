class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
            
        result = []
        stack = [root] # Инициализируем стек корневым узлом
        
        while stack:
            node = stack.pop()       # Извлекаем верхний узел
            result.append(node.val)  # Обрабатываем корень (ROOT)
            
            # Важно: сперва добавляем правый потомок, потом левый
            # Благодаря стеку (LIFO), левый потомок будет обработан следующим
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return result
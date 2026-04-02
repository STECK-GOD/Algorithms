class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = [] # Список для хранения значений в отсортированном порядке
        
        def inorder(node):
            if node is None: # Базовый случай: достигнут пустой узел
                return
            
            inorder(node.left)      # 1. Рекурсивно обходим левое поддерево (LEFT)
            result.append(node.val) # 2. Обрабатываем текущий узел (ROOT)
            inorder(node.right)     # 3. Рекурсивно обходим правое поддерево (RIGHT)
            
        inorder(root) # Запуск обхода с корня
        return result
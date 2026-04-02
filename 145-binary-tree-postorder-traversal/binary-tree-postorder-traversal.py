class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        stack1 = [root] # Стек для обхода (ROOT -> RIGHT -> LEFT)
        stack2 = []     # Стек для инвертирования результата
        
        while stack1:
            node = stack1.pop()
            stack2.append(node) # Помещаем узел во второй стек
            
            # Сначала добавляем левый, затем правый потомок
            # (так правый будет извлечен из stack1 первым)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        
        result = []
        # Извлекаем из stack2, получая нужный порядок: LEFT -> RIGHT -> ROOT
        while stack2:
            result.append(stack2.pop().val)
            
        return result
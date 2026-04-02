# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        # Поиск удаляемого узла
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Узел найден. 
            # Случай 1 и 2: нет детей или только один потомок
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            # Случай 3: у узла два потомка. Ищем преемника.
            successor = self.findMin(root.right)
            root.val = successor.val # Копируем значение преемника
            # Рекурсивно удаляем самого преемника из правого поддерева
            root.right = self.deleteNode(root.right, successor.val)
            
        return root
    
    # Вспомогательная функция для поиска минимального узла
    def findMin(self, node):
        while node.left:
            node = node.left
        return node
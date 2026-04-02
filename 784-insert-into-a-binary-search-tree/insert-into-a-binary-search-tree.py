# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node = TreeNode(val) # Создаем новый узел
        if root is None:
            return new_node   
        current = root
        while True:
            # Если значение меньше, идем в левое поддерево
            if val < current.val:
                if current.left is None:   # Нашли место для вставки
                    current.left = new_node
                    break
                current = current.left     # Спускаемся ниже
            # Если значение больше, идем в правое поддерево
            else:
                if current.right is None:  # Нашли место для вставки
                    current.right = new_node
                    break
                current = current.right    # Спускаемся ниже       
        return root
        
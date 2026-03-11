class Solution:
    def isValid(self, s: str) -> bool:
        # Словарь для сопоставления закрывающих с открывающими
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []  # Стек для открывающих скобок
        
        for char in s:
            if char in bracket_map:
                # Закрывающая скобка - проверяем соответствие
                top = stack.pop() if stack else '#'
                if bracket_map[char] != top:
                    return False
            else:
                # Открывающая скобка - добавляем в стек
                stack.append(char)
        
        # Строка валидна если стек пуст
        return not stack

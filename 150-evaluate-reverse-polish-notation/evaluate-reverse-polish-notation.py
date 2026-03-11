class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        
        for token in tokens:
            if token in operators:
                # Извлекаем операнды (в обратном порядке!)
                b = stack.pop()  # Правый операнд
                a = stack.pop()  # Левый операнд
                
                if token == '+':
                    result = a + b
                elif token == '-':
                    result = a - b
                elif token == '*':
                    result = a * b
                else:  # '/'
                    result = int(a / b)  # Округление к нулю
                
                stack.append(result)
            else:
                stack.append(int(token))
        
        return stack[0]

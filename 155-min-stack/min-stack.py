class MinStack:
    def __init__(self):
        self.stack = []      # Основной стек
        self.min_stack = []  # Стек минимумов

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Добавляем в min_stack если пуст или val <= минимума
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        # Удаляем из min_stack если равен минимуму
        if popped == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
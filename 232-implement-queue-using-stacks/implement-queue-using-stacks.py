class MyQueue:
    def __init__(self):
        self.in_stack = []   # Для входящих
        self.out_stack = []  # Для исходящих

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self._move_elements()
        return self.out_stack.pop()

    def peek(self) -> int:
        self._move_elements()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack
    
    def _move_elements(self) -> None:
        # Переносим если out_stack пуст
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
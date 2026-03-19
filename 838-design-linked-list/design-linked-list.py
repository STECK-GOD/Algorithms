class ListNode:
    def __init__(self, val: int = 0):
        self.val = val
        self.prev = None
        self.next = None
class MyLinkedList:
    def __init__(self):
        self.head = ListNode(0)  # Фиктивная голова
        self.tail = ListNode(0)  # Фиктивный хвост
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        # Оптимизация: выбираем направление
        if index < self.size // 2:
            current = self.head.next
            for _ in range(index):
                current = current.next
        else:
            current = self.tail.prev
            for _ in range(self.size - 1 - index):
                current = current.prev
        return current.val
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index < 0:
            index = 0
        # Находим узел перед позицией вставки
        if index < self.size // 2:
            pred = self.head
            for _ in range(index):
                pred = pred.next
        else:
            succ = self.tail
            for _ in range(self.size - index):
                succ = succ.prev
            pred = succ.prev
        # Вставляем новый узел
        new_node = ListNode(val)
        new_node.prev = pred
        new_node.next = pred.next
        pred.next.prev = new_node
        pred.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        # Находим узел для удаления
        if index < self.size // 2:
            current = self.head.next
            for _ in range(index):
                current = current.next
        else:
            current = self.tail.prev
            for _ in range(self.size - 1 - index):
                current = current.prev
        # Удаляем узел
        current.prev.next = current.next
        current.next.prev = current.prev
        self.size -= 1

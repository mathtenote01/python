from typing import Any


class Stack(object):
    def __init__(self) -> None:
        self.stack = []

    def push(self, data) -> None:
        self.stack.append(data)

    def pop(self) -> Any:
        if self.stack:
            # popは最後の要素を取り出す.
            return self.stack.pop()
        else:
            return None


class MyQueue(object):
    def __init__(self) -> None:
        self.stack_for_queue = Stack()
        self.stack_for_new = Stack()

    def enqueue(self, data):
        self.stack_for_new.push(data)
        current = self.stack_for_queue.pop()
        while current:
            self.stack_for_new.push(current)
            current = self.stack_for_queue.pop()
        current = self.stack_for_new.pop()
        while current:
            self.stack_for_queue.push(current)
            current = self.stack_for_new.pop()

    def dequeue(self):
        return self.stack_for_queue.pop()


if __name__ == "__main__":
    myqueue = MyQueue()
    myqueue.enqueue(1)
    myqueue.enqueue(2)
    myqueue.enqueue(3)
    myqueue.enqueue(4)
    myqueue.enqueue(5)
    print(myqueue.stack_for_queue.stack)
    print(myqueue.dequeue())

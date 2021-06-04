from typing import Any


class Stack(object):
    def __init__(self) -> None:
        self.stack = []

    def push(self, data) -> None:
        self.stack.append(data)

    def pop(self) -> Any:
        if self.stack:
            return self.stack.pop()

    def peek(self) -> Any:
        current = self.pop()
        self.push(current)
        return current

    def isEmpty(self):
        if self.stack == []:
            return True
        else:
            return False


class SortedStack(object):
    def __init__(self):
        self.tmp_stack = Stack()
        self.sorted_stack = Stack()

    def push(self, data):
        current = self.sorted_stack.peek()

        while current and data > current:
            # print(current)
            self.tmp_stack.push(current)
            self.sorted_stack.pop()
            current = self.sorted_stack.peek()
        self.sorted_stack.push(data)
        current = self.tmp_stack.pop()
        while current:
            self.sorted_stack.push(current)
            current = self.tmp_stack.pop()

    def pop(self):
        return self.sorted_stack.pop()

    def print(self):
        current = self.sorted_stack.pop()
        self.tmp_stack.push(current)
        while current:
            print(current)
            current = self.sorted_stack.pop()
            self.tmp_stack.push(current)

        current = self.tmp_stack.pop()
        self.sorted_stack.push(current)

        while current:
            current = self.tmp_stack.pop()
            self.sorted_stack.push(current)


if __name__ == "__main__":
    sorted_stack = SortedStack()
    sorted_stack.push(5)
    sorted_stack.push(3)
    sorted_stack.push(4)
    sorted_stack.push(1)
    sorted_stack.push(7)
    sorted_stack.print()

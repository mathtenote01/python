from __future__ import annotations
from typing import Any


class Node(object):
    def __init__(self, data_: Any, next_node_: Node = None):
        self.data = data_
        self.next = next_node_


class LinkedList(object):
    def __init__(self, head=None) -> None:
        self.head = head

    def append(self, data_: Any) -> None:
        new_node = Node(data_)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def reverse(self):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        prev = Node(current_node)
        current_node = self.head
        while current_node.next:
            tmpForself = current_node.next
            tmpForprev = prev
            prev = Node(current_node.next.data)
            prev.next = tmpForprev
            current_node = tmpForself
        current_node = prev
        while current_node.next.next:
            current_node = current_node.next
        current_node.next = Node(self.head.data)

        val = LinkedList()
        val.head = prev
        return val

    def isPalindrome(self):
        reversed_list = self.reverse()
        original_node = self.head
        reversed_node = reversed_list.head
        while original_node:
            if original_node.data != reversed_node.data:
                return False
            original_node = original_node.next
            reversed_node = reversed_node.next
        return True


if __name__ == "__main__":
    l_original = LinkedList()
    l_original.append(1)
    l_original.append(2)
    l_original.append(3)
    l_reverse = l_original.reverse()
    l_reverse.print()
    print(l_original.isPalindrome())

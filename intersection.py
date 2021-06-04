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

    def insert(self, data_: Any) -> None:
        new_node = Node(data_)
        new_node.next = self.head
        self.head = new_node

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


def intersection(list_1: LinkedList, list_2: LinkedList) -> LinkedList:
    list_1 = list_1.reverse()
    list_2 = list_2.reverse()
    result = LinkedList()
    # list_1.print()
    # list_2.print()
    current_node_1 = list_1.head
    current_node_2 = list_2.head
    while current_node_1.next and current_node_1.data == current_node_2.data:
        result.append(current_node_1.data)
        current_node_1 = current_node_1.next
        current_node_2 = current_node_2.next
    result = result.reverse()
    return result


if __name__ == "__main__":
    list_1 = LinkedList()
    list_2 = LinkedList()
    list_1.append(3)
    list_1.append(4)
    list_1.append(1)
    list_1.append(3)
    list_2.append(5)
    list_2.append(3)
    list_2.append(1)
    list_2.append(3)
    intersection = intersection(list_1, list_2)
    intersection.print()

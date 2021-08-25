class Node:
    """
    val - значение, которое хранится в элементе списка.
    next - следующий элемент списка.
    """

    def __init__(self, _val, _next=None, _prev=None):
        self.val = _val
        self.next = _next
        self.prev = _prev


def Delete(node):
    result = node.val
    return result


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def output_list(self):
        current_node = self.head
        output = []

        while current_node:
            output.append(current_node.val)
            current_node = current_node.next
        return output

    def report(self):
        print(self.output_list())

    def isEmpty(self):
        return self.head is None

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def pushFront(self, value):
        newNode = Node(value)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def pushBack(self, value):
        if self.isEmpty():
            self.pushFront(value)
        else:
            newNode = Node(value)
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode

    def popFront(self):
        old_head = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None

        return Delete(old_head)

    def popBack(self):
        if self.tail.prev is None:
            return self.popFront()

        old_tail = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        return Delete(old_tail)

    def insertAfter(self, node, value):

        if node == self.tail:
            self.pushBack(value)
            return self.tail

        new_node = Node(value)
        new_node.next = node.next
        new_node.prev = node
        node.next = new_node
        new_node.next.prev = new_node

        return new_node

    def insertBefore(self, node, value):
        if not node.prev is None:
            return self.insertAfter(node.prev, value)
        else:
            self.pushFront(value)
            return self.get_head()

    def erase(self, node):
        if node.prev is None:
            return self.popFront()
        elif node.next is None:
            return self.popBack()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            return Delete(node)

    def find(self, value):
        current_node = self.head

        while current_node:
            if current_node.val == value:
                return current_node
            current_node = current_node.next

        return None


def TestPushFront():
    list1 = DoubleLinkedList()
    assert list1.isEmpty() is True
    assert list1.get_head() is None
    assert list1.get_tail() is None

    list1.pushFront(1)
    assert list1.isEmpty() is False
    assert not list1.get_head() is None
    assert list1.get_head().val == 1
    assert list1.get_head().next is None
    assert list1.get_head() == list1.get_tail()

    list1.pushFront(2)
    assert list1.isEmpty() is False
    assert not list1.get_head() is None
    assert list1.get_head().val == 2
    assert not list1.get_tail() is None
    assert list1.get_tail().val == 1
    assert list1.get_tail().next is None

    list1.pushFront(3)
    assert list1.output_list() == [3, 2, 1]

    list1.pushFront(4)
    assert list1.output_list() == [4, 3, 2, 1]

    list1.pushFront(5)
    assert list1.output_list() == [5, 4, 3, 2, 1]

    list1.pushFront(1)
    assert list1.output_list() == [1, 5, 4, 3, 2, 1]
    assert list1.get_tail().val == 1

    print("TestPushFront OK")


def TestPushBack():
    list1 = DoubleLinkedList()
    assert list1.isEmpty() is True
    assert list1.get_head() is None
    assert list1.get_tail() is None

    list1.pushBack(1)
    assert list1.isEmpty() is False
    assert not list1.get_head() is None
    assert list1.get_head().val == 1
    assert list1.get_head().next is None
    assert list1.get_head() == list1.get_tail()

    list1.pushBack(2)
    assert list1.isEmpty() is False
    assert not list1.get_head() is None
    assert list1.get_head().val == 1
    assert not list1.get_tail() is None
    assert list1.get_tail().val == 2
    assert list1.get_tail().next is None

    list1.pushBack(3)
    assert list1.output_list() == [1, 2, 3]

    list1.pushBack(4)
    assert list1.output_list() == [1, 2, 3, 4]

    list1.pushBack(5)
    assert list1.output_list() == [1, 2, 3, 4, 5]

    list1.pushBack(1)
    assert list1.output_list() == [1, 2, 3, 4, 5, 1]
    assert list1.get_tail().val == 1

    print("TestPushBack OK")


def TestPushAndPopBackAndFront():
    list1 = DoubleLinkedList()

    for i in range(1, 6):
        list1.pushFront(-i)
        list1.pushBack(i)

    assert list1.output_list() == [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
    assert list1.get_tail().val == 5

    for i in reversed(range(1, 6)):
        assert list1.popFront() == -i
        assert list1.popBack() == i

    assert list1.isEmpty() is True

    print("TestPushAndPopBackAndFront OK")


def TestInsertAfter():
    list1 = DoubleLinkedList()
    list1.pushBack(1)
    list1.pushBack(2)

    list1.insertAfter(list1.get_head(), 3)
    assert list1.output_list() == [1, 3, 2]

    list1.insertAfter(list1.get_head(), 4)
    assert list1.output_list() == [1, 4, 3, 2]

    list1.insertAfter(list1.get_tail(), 5)
    assert list1.output_list() == [1, 4, 3, 2, 5]
    assert list1.get_tail().val == 5

    node = list1.get_head().next.next
    assert not node is None
    assert node.val == 3

    list1.insertAfter(node, 6)
    node = list1.insertAfter(node, 7)
    assert list1.output_list() == [1, 4, 3, 7, 6, 2, 5]

    node = list1.insertAfter(node, 8)
    node = list1.insertAfter(node, 9)

    print("TestInsertAfter OK")


def TestInsertBefore():
    list1 = DoubleLinkedList()

    list1.pushBack(1)
    list1.pushBack(2)
    list1.insertBefore(list1.get_head(), 3)
    assert list1.output_list() == [3, 1, 2]

    list1.insertBefore(list1.get_tail(), 5)
    assert list1.output_list() == [3, 1, 5, 2]

    node = list1.get_head().next.next
    assert not node is None
    assert node.val == 5
    list1.insertBefore(node, 6)
    list1.insertBefore(node, 7)
    assert list1.output_list() == [3, 1, 6, 7, 5, 2]

    print("TestInsertBefore OK")


def TestPopFront():
    list1 = DoubleLinkedList()

    for i in range(1, 6):
        list1.pushBack(i)

    assert list1.isEmpty() is False
    assert list1.popFront() == 1
    assert not list1.get_head() is None
    assert list1.get_head().val == 2

    for i in range(2, 6):
        assert list1.popFront() == i

    assert list1.get_tail() is None
    assert list1.isEmpty()

    print("TestPopFront OK")


def TestPopBack():
    list1 = DoubleLinkedList()

    for i in range(1, 6):
        list1.pushBack(i)

    assert list1.isEmpty() is False
    assert list1.popBack() == 5
    assert not list1.get_tail() is None
    assert list1.get_tail().val == 4

    for i in reversed(range(1, 5)):
        assert list1.popBack() == i

    assert list1.get_tail() is None
    assert list1.isEmpty()

    print("TestPopBack OK")


def TestErase():
    list1 = DoubleLinkedList()

    for i in range(1, 8):
        list1.pushBack(i)

    assert not list1.isEmpty()
    assert list1.erase(list1.get_head()) == 1
    assert not list1.isEmpty() and not list1.get_head() is None
    assert list1.get_head().val == 2

    assert not list1.isEmpty()
    assert list1.erase(list1.get_tail()) == 7
    assert not list1.isEmpty() and not list1.get_tail() is None
    assert list1.get_tail().val == 6

    node = list1.get_head().next.next
    assert not node is None
    assert node.val == 4

    assert list1.erase(node) == 4
    assert list1.output_list() == [2, 3, 5, 6]
    assert list1.erase(list1.get_head().next) == 3
    assert list1.output_list() == [2, 5, 6]
    assert list1.erase(list1.get_tail()) == 6
    assert list1.output_list() == [2, 5]
    assert list1.erase(list1.get_head()) == 2
    assert list1.output_list() == [5]
    assert list1.erase(list1.get_head()) == 5

    assert list1.isEmpty()

    print("TestErase OK")


if __name__ == "__main__":
    TestPushFront()
    TestPushBack()
    TestPushAndPopBackAndFront()
    TestInsertAfter()
    TestInsertBefore()
    TestPopFront()
    TestPopBack()
    TestErase()

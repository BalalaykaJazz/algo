
class Node:
    """
    val - значение, которое хранится в элементе списка.
    next - следующий элемент списка.
    """
    def __init__(self, _val, _next=None):
        self.val = _val
        self.next = _next


class LinkedList:
    def __init__(self):
        self.head = None

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

    def pushFront(self, value):
        self.head = Node(value, self.head)

    def popFront(self):
        old_head = self.head
        result = old_head.val
        self.head = self.head.next
        return result

    def insertAfter(self, node, value):
        node.next = Node(_val=value, _next=node.next)
        return node.next

    def eraseAfter(self, node):
        to_erase = node.next
        node.next = to_erase.next
        result = to_erase.val
        return result

    def find(self, value):
        current_node = self.head

        while current_node:
            if current_node.val == value:
                return current_node
            current_node = current_node.next

        return None


def TestPushFront():
    """Тестирование функции добавления в голову списка."""

    list1 = LinkedList()
    assert list1.isEmpty() is True
    assert list1.get_head() is None

    list1.pushFront("one")
    assert list1.isEmpty() is False
    assert not list1.get_head() is None
    assert list1.get_head().val == "one"
    assert list1.get_head().next is None

    list1.pushFront("two")
    assert list1.isEmpty() is False
    assert not list1.get_head() is None
    assert list1.get_head().val == "two"

    list1.pushFront("three")
    assert list1.output_list() == ["three", "two", "one"]

    list1.pushFront("four")
    assert list1.output_list() == ["four", "three", "two", "one"]

    list1.pushFront("one")
    assert list1.output_list() == ["one", "four", "three", "two", "one"]

    print("TestPushFront OK")


def TestPopFront():
    """Тестирование функции удаления из головы списка."""

    list1 = LinkedList()

    for i in range(1, 6):
        list1.pushFront(i)

    assert list1.isEmpty() is False
    assert list1.popFront() == 5
    assert not list1.get_head() is None
    assert list1.get_head().val == 4

    for i in reversed(range(1, 5)):
        assert list1.popFront() == i

    assert list1.isEmpty() is True

    print("TestPopFront OK")


def TestInsertAfter():
    """Тестирование функции вставки после указанного элемента"""

    list1 = LinkedList()
    list1.pushFront(2)
    list1.pushFront(1)
    assert list1.output_list() == [1, 2]

    list1.insertAfter(list1.get_head(), 3)
    assert list1.output_list() == [1, 3, 2]

    list1.insertAfter(list1.get_head(), 4)
    assert list1.output_list() == [1, 4, 3, 2]

    node = list1.get_head().next.next
    assert node
    assert node.val == 3

    list1.insertAfter(node, 6)
    node = list1.insertAfter(node, 7)
    assert list1.output_list() == [1, 4, 3, 7, 6, 2]

    node = list1.insertAfter(node, 8)
    list1.insertAfter(node, 9)
    assert list1.output_list() == [1, 4, 3, 7, 8, 9, 6, 2]

    print("TestInsertAfter OK")


def TestEraseAfter():
    """Тестирование функции удаления после указанного элемента."""

    list1 = LinkedList()

    for i in [7, 6, 5, 4, 3, 2, 1]:
        list1.pushFront(i)

    assert list1.isEmpty() is False
    assert list1.eraseAfter(list1.get_head()) == 2

    node = list1.get_head().next.next
    assert node
    assert node.val == 4

    assert list1.eraseAfter(node) == 5
    assert list1.eraseAfter(node) == 6
    assert list1.eraseAfter(node) == 7

    print("TestEraseAfter OK")


def TestFind():
    """Тестирование функции поиска значения в списке."""

    list1 = LinkedList()

    for i in [7, 6, 5, 4, 3, 2, 1]:
        list1.pushFront(i)

    assert list1.find(1) == list1.get_head()
    assert list1.find(3) == list1.get_head().next.next
    assert list1.find(15) is None

    print("TestFind OK")


if __name__ == "__main__":
    TestPushFront()
    TestPopFront()
    TestInsertAfter()
    TestEraseAfter()
    TestFind()

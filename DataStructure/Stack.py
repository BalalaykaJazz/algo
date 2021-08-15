from DataStructure.LinkedList import LinkedList


class Stack:

    def __init__(self):
        self.data_ = LinkedList()

    def push(self, x):
        self.data_.pushFront(x)

    def pop(self):
        if self.data_.isEmpty():
            raise Exception("Trying to pop empty stack")

        return self.data_.popFront()

    def isEmpty(self):
        return self.data_.isEmpty()


def TestStackOps():
    """Тестирование операций над стеком. Стек построен на базе односвязного списка."""

    st = Stack()
    assert st.isEmpty() is True

    st.push(1)
    assert st.isEmpty() is False

    st.push(2)
    st.push(3)
    st.push(4)
    st.push(5)

    assert st.isEmpty() is False
    assert st.pop() == 5
    assert st.pop() == 4
    assert st.pop() == 3
    assert st.pop() == 2
    assert st.pop() == 1
    assert st.isEmpty() is True

    print("TestStackOps OK")


if __name__ == "__main__":
    TestStackOps()

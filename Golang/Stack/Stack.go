// Stack представляет собой реализацию стека
package main

import "fmt"

type node struct {
	val int
	next *node
}

type MyStack struct {
	head *node
}

// Constructor возвращает экземпляр стека.
func Constructor() MyStack {
	return MyStack{}
}

// PushBack добавляет элемент в стек.
func (m *MyStack) PushBack(val int) {
	m.head = &node{val: val, next: m.head}
}

// Pop удаляет элемент из стека.
func (m *MyStack) Pop() {
	if m.head == nil {
		return
	} else if m.head.next == nil {
		m.head = nil
		return
	}

	m.head = m.head.next
}

// PrintMyStack выводит содержимое стека в стандартный вывод.
func (m *MyStack) PrintMyStack() {
	head := m.head

	if head == nil {
		fmt.Println("-> Empty stack!")
	} else {
		for head != nil {
			fmt.Printf("%d -> ", head.val)
			head = head.next
		}
		fmt.Println()
	}
}

func main() {
	obj := Constructor()
	obj.PrintMyStack()
	obj.PushBack(1)
	obj.PushBack(2)
	obj.PushBack(3)
	obj.PushBack(5)
	obj.PrintMyStack()
	obj.Pop()
	obj.Pop()
	obj.Pop()
	obj.PrintMyStack()
	obj.Pop()
	obj.PrintMyStack()
}

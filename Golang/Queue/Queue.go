// Queue представляет собой реализацию очереди
package main

import "fmt"

type node struct {
	val int
	next *node
}

type MyQueue struct {
	head *node
}

// Constructor возвращает экземпляр очереди.
func Constructor() MyQueue {
	return MyQueue{}
}

// PushFront добавляет элемент в конец очереди.
func (m *MyQueue) PushFront(val int) {
	m.head = &node{val: val, next: m.head}
}

// Pop удаляет элемент из начала очереди.
func (m *MyQueue) Pop() {
	if m.head == nil {
		return
	} else if m.head.next == nil {
		m.head = nil
		return
	}

	current := m.head
	for (current.next) != nil {
		if current.next.next == nil {
			break
		}
		current = current.next
	}

	current.next = nil
}

// PrintMyQueue выводит содержимое очереди в стандартный вывод.
func (m *MyQueue) PrintMyQueue() {
	head := m.head

	if head == nil {
		fmt.Println("-> Empty queue!")
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
	obj.PrintMyQueue()
	obj.PushFront(1)
	obj.PushFront(2)
	obj.PushFront(3)
	obj.PushFront(5)
	obj.PrintMyQueue()
	obj.Pop()
	obj.Pop()
	obj.Pop()
	obj.PrintMyQueue()
	obj.Pop()
	obj.PrintMyQueue()
}

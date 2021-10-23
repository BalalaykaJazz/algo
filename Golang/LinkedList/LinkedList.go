// LinkedList представляет произвольную реализацию односвязного списка
package main

import (
	"fmt"
)

type node struct {
	val int
	next *node
}

type MyLinkedList struct {
	head *node
}

// Constructor возвращает экземпляр списка.
func Constructor() MyLinkedList {
	return MyLinkedList{}
}

// AddAtHead добавляет элемент в начало списка.
func (m *MyLinkedList) AddAtHead(val int)  {
	m.head = &node{val: val, next: m.head}
}

// AddAtTail добавлет элемент в конец списка.
func (m *MyLinkedList) AddAtTail(val int) {
	if m.head == nil {
		m.AddAtHead(val)
	} else {
		current := m.head
		for current.next != nil {
			current = current.next
		}

		current.next = &node{val: val}

	}
}

// findElementBeforeIndex Возвращает элемент стоящий в списке перед указанным индексом.
func (m *MyLinkedList) findElementBeforeIndex(index int) *node {
	if index < 0 {
		return nil
	}

	current := m.head
	for ; index > 1; index-- {
		if current == nil {
			continue
		}
		current = current.next
	}
	return current
}

// Get возвращает значение элемента списка найденного по индексу или -1 если элемент не был найден.
func (m *MyLinkedList) Get(index int) int {
	if index < 0 || m.head == nil {
		return -1
	} else if index == 0 {
		return m.head.val
	} else {
		current := m.findElementBeforeIndex(index)

		if current == nil || current.next == nil {
			return -1
		} else {
			return current.next.val
		}
	}
}

// AddAtIndex добавляет элемент в позицию перед индексом, если индекс корректный.
func (m *MyLinkedList) AddAtIndex(index int, val int)  {
	if index < 0 {
		return
	} else if index == 0 {
		m.AddAtHead(val)
		return
	}

	current:= m.findElementBeforeIndex(index)
	if current != nil {
		current.next = &node{val: val, next: current.next}
	}
}

// DeleteAtIndex удаляет элемент по индексу, если индекс корректный.
func (m *MyLinkedList) DeleteAtIndex(index int) {
	if index < 0 || m.head == nil {
		return
	} else if index == 0 {
		if m.head.next == nil {
			m.head = nil
		} else {
			m.head = m.head.next
		}
	} else {
		current := m.findElementBeforeIndex(index)

		if current != nil{
			if current.next != nil {
				current.next = current.next.next
			} else  {
				current.next = nil
			}
		}
	}
}

// PrintLinkedList выводит содержимое списка в стандартный вывод.
func (m *MyLinkedList) PrintLinkedList() {
	head := m.head

	if head == nil {
		fmt.Println("-> Empty list!")
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
	obj.AddAtHead(3)
	obj.AddAtHead(7)
}

package main

import (
	"reflect"
	"testing"
)

func checkGet(t *testing.T, obj *MyLinkedList, index int, expected int) {
	valueFromGet := obj.Get(index)
	if valueFromGet != expected {
		t.Errorf("%q not equal to expected %q",  valueFromGet, expected)
	}
}

func checkList(t *testing.T, obj *MyLinkedList, expected []int) {
	var valueFromList []int
	head := obj.head
	for head != nil {
		valueFromList = append(valueFromList, head.val)
		head = head.next
	}

	if !reflect.DeepEqual(valueFromList, expected) {
		t.Errorf("%q not equal to expected %q",  valueFromList, expected)
	}
}

func TestAddAtIndex(t *testing.T) {
	obj := Constructor()
	obj.AddAtIndex(0, 10)
	obj.AddAtIndex(0, 20)
	obj.AddAtIndex(1, 30)

	checkList(t, &obj, []int{20, 30, 10})
	checkGet(t, &obj, 0, 20)
}

func TestMyLinkedList(t *testing.T) {
	obj := Constructor()
	obj.AddAtHead(3)
	obj.AddAtHead(7)
	obj.AddAtHead(2)

	checkList(t, &obj, []int{2, 7, 3})

	obj.AddAtIndex(1, 4)
	obj.AddAtIndex(2, 5)
	obj.AddAtIndex(0, 1)
	obj.AddAtIndex(6, 42)
	obj.AddAtIndex(999, 999)
	obj.AddAtTail(15)
	obj.AddAtTail(16)

	checkList(t, &obj, []int{1, 2, 4, 5, 7, 3, 42, 15, 16})
	checkGet(t, &obj,0, 1)
	checkGet(t, &obj,1, 2)
	checkGet(t, &obj,8, 16)
	checkGet(t, &obj,99, -1)

	obj.DeleteAtIndex(2)
	obj.DeleteAtIndex(0)
	obj.DeleteAtIndex(6)
	obj.DeleteAtIndex(5)
	obj.DeleteAtIndex(99)

	checkList(t, &obj, []int{2, 5, 7, 3, 42})
}

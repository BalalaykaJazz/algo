package main

import (
	"reflect"
	"testing"
)

func checkQueue(t *testing.T, obj *MyQueue, expected []int) {
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

func TestQueue(t *testing.T) {
	obj := Constructor()
	obj.PushFront(1)
	obj.PushFront(2)
	obj.PushFront(3)
	obj.PushFront(4)
	obj.PushFront(5)
	checkQueue(t, &obj, []int{5, 4, 3, 2, 1})
	obj.Pop()
	obj.Pop()
	obj.Pop()
	checkQueue(t, &obj, []int{5, 4})
	obj.Pop()
	obj.Pop()
	checkQueue(t, &obj, nil)
}

func TestPopFirst(t *testing.T) {
	obj := Constructor()
	obj.Pop()
	checkQueue(t, &obj, nil)

	obj.PushFront(1)
	obj.PushFront(2)
	checkQueue(t, &obj, []int{2, 1})
}

package main

import (
	"reflect"
	"testing"
)

func checkStack(t *testing.T, obj *MyStack, expected []int) {
	var valueFromList []int
	head := obj.head
	for head != nil {
		valueFromList = append(valueFromList, head.val)
		head = head.next
	}

	if !reflect.DeepEqual(valueFromList, expected) {
		t.Errorf("%v not equal to expected %v",  valueFromList, expected)
	}
}

func TestStack(t *testing.T) {
	obj := Constructor()
	obj.PushBack(1)
	obj.PushBack(2)
	obj.PushBack(3)
	obj.PushBack(4)
	obj.PushBack(5)
	checkStack(t, &obj, []int{5, 4, 3, 2, 1})
	obj.Pop()
	obj.Pop()
	obj.Pop()
	checkStack(t, &obj, []int{2, 1})
	obj.Pop()
	obj.Pop()
	checkStack(t, &obj, nil)
}

func TestPopFirst(t *testing.T) {
	obj := Constructor()
	obj.Pop()
	checkStack(t, &obj, nil)

	obj.PushBack(1)
	obj.PushBack(2)
	checkStack(t, &obj, []int{2, 1})
}

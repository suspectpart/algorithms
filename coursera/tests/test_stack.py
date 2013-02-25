from nose.tools import *
from stack import Stack

def test_empty_stack():
	s = Stack()
	assert_equals(s.is_empty(), True)
	assert_equals(s.count(), 0)
	assert_equals(s.pop(), None)

def test_stack_with_one_item():
	s = Stack()
	s.push(1)
	assert_equals(s.pop(), 1)
	assert_equals(s.pop(), None)

def test_stack_with_more_items():
	s = Stack()
	s.push(1)
	s.push(2)
	s.push(3)
	assert_equals(s.pop(), 3)
	assert_equals(s.pop(), 2)
	assert_equals(s.pop(), 1)
	assert_equals(s.pop(), None)
	
def test_stack_count():
	s = Stack()
	assert_equals(s.count(), 0)
	s.push(1)
	assert_equals(s.count(), 1)
	s.pop()
	assert_equals(s.count(), 0)
	
def test_is_empty():
	s = Stack()
	assert_equals(s.is_empty(), True)
	s.push(1)
	assert_equals(s.is_empty(), False)
	s.pop()
	assert_equals(s.is_empty(), True)
	
def test_peek():
	s = Stack()
	assert_equals(s.peek(), None)
	s.push(1)
	assert_equals(s.peek(), 1)
	assert_equals(s.count(), 1)
	assert_equals(s.pop(), 1)
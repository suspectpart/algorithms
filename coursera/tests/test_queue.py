from nose.tools import *
from queue import Queue

def test_empty_queue():
	queue = Queue()
	eq_(queue.is_empty(),True)
	eq_(queue.dequeue(), None)

def test_enqueue_dequeue_one_item():
	queue = Queue()
	queue.enqueue(5)	
	eq_(queue.is_empty(),False)
	eq_(queue.dequeue(), 5)
	eq_(queue.is_empty(),True)
	eq_(queue.dequeue(), None)

def test_multiple_enqueues_dequeues():
	queue = Queue()
	queue.enqueue(5)	
	queue.enqueue(6)	
	queue.enqueue(7)	
	eq_(queue.dequeue(), 5)
	eq_(queue.dequeue(), 6)
	eq_(queue.dequeue(), 7)
	eq_(queue.dequeue(), None)	

def test_multiple_empty_dequeues():
	queue = Queue()
	eq_(queue.is_empty(), True)
	eq_(queue.dequeue(), None)
	eq_(queue.dequeue(), None)
	eq_(queue.dequeue(), None)
	eq_(queue.is_empty(), True)
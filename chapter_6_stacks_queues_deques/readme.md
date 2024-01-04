# Chapter 6 Stacks, Queues and Deques

## Stacks

A stack is a collection of objects that are inserted and removed according to the
last-in, first-out (LIFO) principle. A user may insert objects into a stack at any
time, but may only access or remove the most recently inserted object that remains
(at the so-called “top” of the stack).

Formally, a stack is an abstract data type (ADT) such that an instance S supports the following two methods:

- `S.push(e)`: Add element e to the top of stack S.
- `S.pop()`: Remove and return the top element from the stack S; an error occurs if the stack is empty.

Additionally, we can define the following accessor methods:  

- `S.top()`: Return a reference to the top element of stack S, without removing it; an error occurs if the stack is empty.
- `S.is_empty()`: Return True if stack S does not contain any elements.
- `len(S)`: Return the number of elements in stack S; in Python, we implement this with the special method `__len__`.

### Array-Based Stack implementation

A simple way to implement a stack is to use a Python list. The last element of the list will represent the top of the stack.

- **Cost analysis table:**

| Operation | Running Time |
| --------- |-------------|
| `S.push(e)` | $O(1)$      |
| `S.pop()` | $O(1)$      |
| `S.top()` | $O(1)$      |
| `S.is_empty()` | $O(1)$      |
| `len(S)` | $O(1)$      |

*Space usage:* $O(n)$


## Queues

Another fundamental data structure is the queue. It is a close “cousin” of the stack,
as a queue is a collection of objects that are inserted and removed according to the
first-in, first-out (FIFO) principle. That is, elements can be inserted at any time,
but only the element that has been in the queue the longest can be next removed.

Formally, the queue abstract data type defines a collection that keeps objects in a
sequence, where element access and deletion are restricted to the first element in
the queue, and element insertion is restricted to the back of the sequence. This
restriction enforces the rule that items are inserted and deleted in a queue according to 
the first-in, first-out (FIFO) principle. The queue abstract data type (ADT)
supports the following two fundamental methods for a queue Q:

- `Q.enqueue(e)`: Add element e to the back of queue Q.
- `Q.dequeue()`: Remove and return the first element from queue Q; an error occurs if the queue is empty.

Additionally, we can define the following accessor methods:

- `Q.first()`: Return a reference to the element at the front of queue Q, without removing it; an error occurs if the queue is empty.
- `Q.is_empty()`: Return True if queue Q does not contain any elements.
- `len(Q)`: Return the number of elements in queue Q; in Python, we implement this with the special method `__len__`.

### Array-Based Queue implementation

We can use a circular array to implement a queue. The front of the queue is at position `f`, and the rear of the queue
is at position `r`. When an element is first enqueued, it is placed within the array at position `f`. If the queue
contains `n` elements, then the next element to be dequeued will be at position `(f + 1) % N`, where `N` is the
capacity of the array. 

![Array-based queue](https://courses.cs.washington.edu/courses/cse326/00wi/handouts/lecture1/img017.gif)

- **Cost analysis table:**

| Operation | Running Time |
| --------- |-------------|
| `Q.enqueue(e)` | $O(1)$      |
| `Q.dequeue()` | $O(1)$      |
| `Q.first()` | $O(1)$      |
| `Q.is_empty()` | $O(1)$      |
| `len(Q)` | $O(1)$      |

*Space usage:* $O(n)$

## Deque: Double-Ended Queues

A deque, also known as a double-ended queue, is an ordered collection of elements similar to the queue. 
It has two ends, a front and a rear, and the items remain positioned in the collection. What makes a deque different 
is the unrestrictive nature of adding and removing items. New items can be added at either the front or the rear. 
Likewise, existing items can be removed from either end. In a sense, this hybrid linear structure provides 
all the capabilities of stacks and queues in a single data structure.

![Deque](https://i.stack.imgur.com/VCp4b.jpg)

To provide a symmetrical abstraction, the deque ADT is defined so that deque D
supports the following methods:

- `D.add_first(e)`: Add element e to the front of deque D.
- `D.add_last(e)`: Add element e to the back of deque D.
- `D.delete_first()`: Remove and return the first element from deque D; an error occurs if the deque is empty.
- `D.delete_last()`: Remove and return the last element from deque D; an error occurs if the deque is empty.

Additionally, we can define the following accessor methods:

- `D.first()`: Return (but do not remove) the first element of deque D; an error occurs if the deque is empty.
- `D.last()`: Return (but do not remove) the last element of deque D; an error occurs if the deque is empty.
- `D.is_empty()`: Return True if deque D does not contain any elements.
- `len(D)`: Return the number of elements in deque D; in Python, we implement this with the special method `__len__`.

### Array-Based Deque implementation

We can implement the deque ADT in much the same way as the ArrayQueue class.
Whenever we need to know the back of the deque, or the first available slot beyond the back of the deque, we use the
modular arithmetic operator to perform the calculation.
For example to get the last element of the deque:

`back = (front + size - 1) % len(self._data)`

- **Cost analysis table:**

| Operation | Running Time |
| --------- |-------------|
| `D.add_first(e)` | $O(1)$      |
| `D.add_last(e)` | $O(1)$      |
| `D.delete_first()` | $O(1)$      |
| `D.delete_last()` | $O(1)$      |
| `D.first()` | $O(1)$      |
| `D.last()` | $O(1)$      |
| `D.is_empty()` | $O(1)$      |
| `len(D)` | $O(1)$      |

*Space usage:* $O(n)$
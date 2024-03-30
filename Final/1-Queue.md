# Queue

## Introduction

In computer science, a **queue** is a linear data structure that follows the First In, First Out (FIFO) principle. It means that the element that is added first to the queue will be the one to be removed first. Queues are widely used in various applications such as operating systems, networking, and simulations.

## What is a Queue?

A queue is a collection of elements that supports two basic operations:

1. **Enqueue**: Adds an element to the rear of the queue.
2. **Dequeue**: Removes an element from the front of the queue.

## FIFO Principle

FIFO stands for "First In, First Out." It's a principle or concept that describes the order in which elements are processed or accessed in a data structure. In a FIFO data structure, the first element added to the structure will be the first one to be removed.

## Implementations of Queue:

In Python, you can implement a queue using a list. Although it's not the most efficient way since adding or removing elements from the beginning of a list is O(n) operation due to shifting all elements, here is how you would do it:

```python
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)
```


## Efficiency of Queue Operations

### Enqueue Operation
In Python, appending an element to the end of a list using the `append()` method takes constant time on average, denoted as O(1).

### Dequeue Operation
In Python, using `pop(0)` to remove the first element of a list has a time complexity of O(n), where n is the number of elements in the queue.

### Size Checking
Checking the size of the queue is efficient in Python, typically taking constant time regardless of the number of elements. This is done using the `len()` function.


## Image of Queue Data Structure

![Alt text](images/Queue-Img1.png)
Here is a great image I found representing how a queue works. The link for the website is [here](https://www.geeksforgeeks.org/queue-data-structure/).


## Challenge: Implementing a Circular Queue

A circular queue is a variation of the standard queue data structure in which the last element is connected back to the first element, forming a circular arrangement. This allows for efficient utilization of memory and avoids the need for shifting elements when dequeuing.

Your challenge is to implement a circular queue in Python. You need to define a class `CircularQueue` with the following methods:

- `enqueue(self, item)`: Adds an element to the rear of the circular queue.
- `dequeue(self)`: Removes an element from the front of the circular queue.
- `is_empty(self)`: Returns True if the circular queue is empty, False otherwise.
- `is_full(self)`: Returns True if the circular queue is full, False otherwise.

You should handle the case when the circular queue becomes full, and attempting to enqueue more elements should result in an error or resizing the queue if needed.
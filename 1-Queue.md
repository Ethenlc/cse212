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
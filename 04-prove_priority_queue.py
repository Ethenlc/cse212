"""
CSE212 
(c) BYU-Idaho
04-Prove - Problem 2

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

class Priority_Queue:
    """
    This queue follows the same FIFO process except that higher priority
    nodes will be dequeued before lower priority nodes.  Nodes of the same
    priority will follow the same FIFO process.
    """

    class Node:
        """
        Each node is the queue will have both a value and a priority.
        """

        def __init__(self, value, priority):
            """
            Initialize a new node
            """
            self.value = value
            self.priority = priority

        def __str__(self):
            """
            Display a single node
            """
            return "{} (Pri:{})".format(self.value, self.priority)

    def __init__(self):
        """ 
        Initialize an empty priority queue
        """
        self.queue = []

    def enqueue(self, value, priority):
        """
        Add a new value to the queue with an associated priority.  The
        node is always added to the back of the queue irregardless of 
        the priority.
        """
        new_node = Priority_Queue.Node(value, priority)
        self.queue.append(new_node)

    def dequeue(self):
        """
        Remove the next value from the queue based on the priority.  The 
        highest priority item will be removed.  In the case of multiple
        values with the same high priority, the one closest to the front
        (in traditional FIFO order) will be removed.  Priority values are
        interpreted as higher numbers have higher priority.  For example, 
        10 is a higher priority than 5.
        """
        if len(self.queue) == 0:  # Verify the queue is not empty
            print("The queue is empty.")
            return None

        # Find the index of the item with the highest priority to remove
        high_pri_index = 0
        for index in range(1, len(self.queue)):
            if self.queue[index].priority > self.queue[high_pri_index].priority:
                high_pri_index = index
            elif self.queue[index].priority == self.queue[high_pri_index].priority:
                # If priorities are equal, compare the order of insertion (FIFO)
                if self.queue[index].value < self.queue[high_pri_index].value:
                    high_pri_index = index

        # Remove and return the item with the highest priority
        value = self.queue.pop(high_pri_index).value
        return value
        
    def __len__(self):
        """
        Support the len() function
        """
        return len(self.queue)

    def __str__(self):
        """ 
        Support the str() function to provide a string representation of the
        priority queue.  This is useful for debugging.  If you have a 
        Priority_Queue object called pq, then you run print(pq) to see the 
        contents.
        """
        result = "["
        for node in self.queue:
            result += str(node)  # This uses the __str__ from the Node class
            result += ", "
        result += "]"
        return result

# Test Cases

# Test 1
# Scenario: Test an empty queue.
# Expected Result: "0 The queue is empty."
print("Test 1")
pq = Priority_Queue()
print(len(pq))
pq.dequeue()

print("=================")

# Test 2
# Scenario: Add a task to the queue. Remove it and make sure that the one removed is correct. Print the length and make sure it's 0.
# Expected Result: "Dequeued value: Task 1. Length of queue after dequeue:"
print("Test 2")
pq = Priority_Queue()
pq.enqueue("Task 1", 3)

dequeued_value = pq.dequeue()
print("Dequeued value:", dequeued_value)  # Print the value returned by dequeue
print("Length of queue after dequeue:", len(pq))  # Print the length of the queue after dequeue
print(len(pq))

print("=================")
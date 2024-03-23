# Tree

## Introduction

In computer science, a **tree** is a hierarchical data structure consisting of nodes connected by edges. Each node has a parent node and zero or more child nodes. Trees are used to represent hierarchical relationships and are widely used in computer science for various applications such as representing file systems, organizing data, and implementing search algorithms.

## What is a Tree?

A tree is a collection of nodes organized in a hierarchical structure. It consists of the following components:

- **Node**: Each element in a tree is called a node. Nodes are connected by edges.
- **Root**: The topmost node in a tree is called the root node. It's the starting point of the tree.
- **Parent**: A node that has child nodes connected to it is called a parent node.
- **Child**: Nodes directly connected to another node are called its child nodes.
- **Leaf**: Nodes that do not have any child nodes are called leaf nodes or terminal nodes.
- **Edge**: The connection between nodes in a tree is called an edge.

## Implementation of Tree

In Python, you can implement a tree using classes and objects. Each node in the tree can be represented as an object with references to its child nodes.

```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)
```

## Tree Traversal
Tree traversal refers to visiting all the nodes in a tree in a specific order. There are two common methods for tree traversal:

- Depth-First Traversal: Visits nodes starting from the root and explores as far as possible along each branch before backtracking.
- Breadth-First Traversal: Visits nodes level by level, starting from the root.

### Common Tree Operations

#### Insertion

Inserting a new node into a tree involves finding the appropriate location to place the new node. This typically involves traversing the tree based on some criteria (e.g., comparing node values) until a suitable position is found.

#### Deletion

Deleting a node from a tree requires finding the node to be deleted and then removing it from the tree. The deletion process may vary depending on whether the node to be deleted is a leaf node, has only one child, or has multiple children.

```python
# The following is initializing the class TreeNode
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def insert(self, new_node):
        self.children.append(new_node)

    def remove_child(self, child_node):
        self.children.remove(child_node)

    def delete(self, target):
        for child in self.children:
            if child.data == target:
                self.remove_child(child)
                return True
            else:
                if child.delete(target):
                    return True
        return False

# Example usage
if __name__ == "__main__":
    # Create a tree
    root = TreeNode('A')
    root.add_child(TreeNode('B'))
    root.add_child(TreeNode('C'))
    
    # Insert a new node
    new_node = TreeNode('D')
    root.children[0].insert(new_node)

    # Print tree before deletion
    print("Tree before deletion:")
    print("Root:", root.data)
    for child in root.children:
        print("Child:", child.data)

    # Delete a node
    root.delete('C')

    # Print tree after deletion
    print("\nTree after deletion:")
    print("Root:", root.data)
    for child in root.children:
        print("Child:", child.data)
```
## Linked List in Python
A linked list is a linear data structure where each node contains a reference to an object and a reference to the next node in the list. In this implementation, the linked list is implemented as a singly linked list.

### Class Definition
The linked list implementation is defined in a class called `LinkedList`. The class contains the following methods:

#### `__init__(self)`
This is the constructor method for the LinkedList class. It initializes the linked list with an empty head node.

#### `display(self)`
This method is used to display the elements of the linked list. It iterates through the linked list and prints out each node's data.

#### `append(self, data)`
This method adds an element to the end of the linked list. The new node's data is set to the input data and its next pointer is set to `None`.

#### `prepend(self, data)`
This method adds an element to the front of the linked list. The new node's data is set to the input data, its next pointer is set to the current head node, and the head node is updated to the new node.

#### `insert_after_node(self, prev_node, data)`
This method inserts a new node with the input data after the specified node. The new node's data is set to the input data and its next pointer is set to the next node of the specified node. The next node of the specified node is then updated to the new node.

#### `delete_node(self, key)`
This method deletes a node with the input key from the linked list. It iterates through the linked list and deletes the node if its data matches the input key.

#### `delete_node_at_pos(self, pos)`
This method deletes the node at the specified position from the linked list. It iterates through the linked list and deletes the node if the current position matches the input position.

#### `len_iterative(self)`
This method returns the length of the linked list using iteration. It iterates through the linked list and increments a counter until the end of the linked list is reached.

#### `len_recursive(self, node)`
This method returns the length of the linked list using recursion. It calls itself with the next node in the linked list until the end of the linked list is reached.

## Testing
Here is an example of how you can use the `LinkedList` class to test the code:


```python
# Initialize a linked list
llist = LinkedList()

# Append elements to the linked list
llist.append("A")
llist.append("B")
llist.append("C")

# Display the linked list
llist.display()
# Output: ['A', 'B', 'C']

# Prepend an element to the linked list
llist.prepend("P")

# Display the linked list
llist.display()
# Output: ['P', 'A', 'B', 'C']

# Insert an element after a specific node
llist.insert_after_node(llist.head.next, "X")

# Display the linked list
llist.display()
# Output: ['P', 'A', 'X', 'B', 'C']

# Delete a node with specific key
llist.delete_node("X")

# Display the linked list
llist.display()
# Output: ['P', 'A', 'B', 'C']

# Delete a node at a specific position
llist.delete_node_at_pos(2)

# Display the linked list
llist.display()
# Output: ['P', 'A', 'C']

# Find the length of the linked list using iteration
print("Length of linked list (iterative): ", llist.len_iterative())
# Output: Length of linked list (iterative): 3

# Find the length of the linked list using recursion
print("Length of linked list (recursive): ", llist.len_recursive(llist.head))
# Output: Length of linked list (recursive): 3

```

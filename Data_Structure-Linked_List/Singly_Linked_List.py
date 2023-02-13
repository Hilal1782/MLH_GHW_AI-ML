#Write code below

# Linked list data structure
# Class to define a node in the linked list
class Node:
    # Initialize a node with its data
    def __init__(self, data):
        self.data = data
        self.next = None

# Class to define a linked list
class LinkedList:
    # Initialize the head of the linked list
    def __init__(self):
        self.head = None

    # Add a node with data to the end of the linked list
    def append(self, data):
        # Create a new node with the given data
        new_node = Node(data)
        # If the linked list is empty, set the head to the new node
        if self.head is None:
            self.head = new_node
            return
        # Otherwise, traverse the linked list to find the last node
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        # Set the next of the last node to the new node
        last_node.next = new_node

    # Add a node with data to the beginning of the linked list
    def prepend(self, data):
        # Create a new node with the given data
        new_node = Node(data)
        # Set the next of the new node to the current head
        new_node.next = self.head
        # Set the head of the linked list to the new node
        self.head = new_node

    # Insert a node with data after a specified node in the linked list
    def insert_after_node(self, prev_node, data):
        # If the previous node is not in the linked list, print an error message
        if not prev_node:
            print("Previous node is not in the list")
            return 
        # Create a new node with the given data
        new_node = Node(data)
        # Set the next of the new node to the next of the previous node
        new_node.next = prev_node.next
        # Set the next of the previous node to the new node
        prev_node.next = new_node

    # Delete a node with the given key from the linked list
    def delete_node(self, key):
        cur_node = self.head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return
        prev = None
        # Traverse the linked list to find the node with the given key
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next
        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None

    # Delete a node at a specified position from the linked list    
    def delete_node_at_pos(self, pos):
        cur_node = self.head  
        if pos == 0:
            self.head = cur_node.next  
            cur_node = None  
            return  

        prev = None
        count = 0  
        # loop through the linked list until current node is None or count is equal to position
        while cur_node and count != pos:  
            prev = cur_node  
            cur_node = cur_node.next 
            count += 1  

        if cur_node is None:  
            return 

        prev.next = cur_node.next  
        cur_node = None

    #Returns the length of the linked list using an iterative approach
    def len_iterative(self):
        count = 0 
        cur_node = self.head  
        while cur_node:  
            count += 1 
            cur_node = cur_node.next  

        return count  
    #Returns the length of the linked list using a recursive approach
    def len_recursive(self, node):
        if node is None:  
            return 0 

        return 1 + self.len_recursive(node.next)  

    #Prints all the elements of the linked list
    def display(self):
        # initialize an empty list to store the elements
        elems = []  
        cur_node = self.head 
        # loop through the linked list until current node is None
        while cur_node:  
            elems.append(cur_node.data) 
            cur_node = cur_node.next  

        print(elems)



# Testing

# Initialize a linked list
llist = LinkedList()

# Append elements to the linked list
llist.append("A")
llist.append("B")
llist.append("C")

# Display the linked list
llist.display()

# Prepend an element to the linked list
llist.prepend("P")

# Display the linked list
llist.display()

# Insert an element after a specific node
llist.insert_after_node(llist.head.next, "X")

# Display the linked list
llist.display()

# Delete a node with specific key
llist.delete_node("X")

# Display the linked list
llist.display()

# Delete a node at a specific position
llist.delete_node_at_pos(2)

# Display the linked list
llist.display()

# Find the length of the linked list using iteration
print("Length of linked list (iterative): ", llist.len_iterative())

# Find the length of the linked list using recursion
print("Length of linked list (recursive): ", llist.len_recursive(llist.head))

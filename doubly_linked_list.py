# Task 1.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"<Node|{self.value}>"
    
# Task 2.

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, new_value):
        new_node = Node(new_value)
        if self.head:
            self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def traverse(self): 
        print('Linked List Elements:')
        print('head\n | \n V')
        current = self.head
        while current:
            print(current, end=' <--> ')
            current = current.next
        print(None)

    def get_node(self, value_to_get): 
        node_to_check = self.head
        while node_to_check:
            if node_to_check.value == value_to_get:
                return node_to_check
            node_to_check = node_to_check.next
        return None

    def delete(self, value_to_delete):
        if self.head is None:
            print('List is empty, nothing to delete')
            return
        if self.head.value == value_to_delete:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        current_node = self.head
        while current_node:
            if current_node.value == value_to_delete:
                if current_node.prev:
                    current_node.prev.next = current_node.next
                if current_node.next:
                    current_node.next.prev = current_node.prev
                return
            current_node = current_node.next
        print(f"{value_to_delete} is not in this Linked List.")


# Task 3.

days = DoublyLinkedList()

days.insert('Wednesday')
days.insert('Sunday')
days.insert('Monday')
days.insert('Tuesday')
days.insert('Thursday')
days.delete('Sunday')
days.delete('Wednesday')

days.traverse()






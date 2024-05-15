# Task 1.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"<Node|{self.value}>"
    
# Task 2.

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_after(self, prev_value, new_value):        
        prev_node = self.get_node(prev_value)
        if prev_node is None:
            print(f"{prev_value} is not in the linked list")
        else:
            new_node = Node(new_value)
            new_node.next = prev_node.next
            prev_node.next = new_node

    def delete(self, value_to_delete):
        if self.head is None:
            print('List is empty, nothing to delete')
            return
        if self.head.value == value_to_delete:
            self.head = self.head.next
            return
        current_node = self.head

        while current_node.next:  
            if current_node.next.value == value_to_delete:   
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
        print(f"{value_to_delete} is not in this Linked List.")

    def traverse(self):
        print('Linked List Elements:')
        print('head\n | \n V')
        current = self.head

        while current:
            print(current, end=' -> ')
            current = current.next
        print(None)

    def get_node(self, value_to_get): 
        node_to_check = self.head
        while node_to_check:
            if node_to_check.value == value_to_get:
                return node_to_check
            node_to_check = node_to_check.next
        return None

    def append(self, new_value): 
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
    

# Task 3.

months = SinglyLinkedList()

months.append('May')
months.insert_after('July', 'August')
months.append('July')
months.insert_after('August','September')
months.append('October')
months.insert_after('May', 'June')
months.append('December')
months.insert_after('October', 'November')
months.delete('September')

months.traverse()







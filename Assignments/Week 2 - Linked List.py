class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        if self.head is None:
            print("The list is empty")
        else:
            current = self.head
            print("Linked list:")
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")

    def delete_n(self, position):
        if self.head is None:
            print("Cannot delete from an empty list")
            return

        if position <= 0:
            print("Invalid position! Position must be 1 or more")
            return

        if position == 1:
            print(f"Deleting node at position 1 with value: {self.head.data}")
            self.head = self.head.next
            return

        current = self.head
        count = 1
        while current and count < position - 1:
            current = current.next
            count += 1

        if current is None or current.next is None:
            print("Position out of range")
        else:
            print(f"Deleting node at position {position} with value: {current.next.data}")
            current.next = current.next.next


if __name__ == "__main__":
    llist = LinkedList()

    llist.add_node(10)
    llist.add_node(20)
    llist.add_node(30)
    llist.add_node(40)

    llist.print_list()

    llist.delete_n(2)
    llist.print_list()

    llist.delete_n(1)
    llist.print_list()

    llist.delete_n(10)

    llist.delete_n(1)
    llist.delete_n(1)
    llist.print_list()

    llist.delete_n(1)

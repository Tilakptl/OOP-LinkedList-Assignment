class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def search(self, data):
        current = self.head

        while current:
            if current.data == data:
                return True
            current = current.next
        return False
my_list = LinkedList()
my_list.append(5)
my_list.append(15)
my_list.append(25)
print("Linked List:")
my_list.display()

value = 15
if my_list.search(value):
    print(value, "found in the list")
else:
    print(value, "not found in the list")
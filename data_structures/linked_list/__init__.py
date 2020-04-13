__author__ = "Niketan Rane"

class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

    def __repr__(self):
        return f"Node{self.item}"

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, item):
        node = Node(item, self.head)
        self.head = node

    def insert_tail(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            while temp.next:
                print(f"temp {temp.item}")
                temp = temp.next
            temp.next = node

    def delete_tail(self):
        temp = self.head
        if temp and temp.next:
            while temp.next.next:
                temp = temp.next
            temp.next = None
        else:
            self.head = None

    def delete_head(self):
        if self.head:
            self.head = self.head.next

    def reverse(self):
        current = self.head
        prev = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def __repr__(self):
        current = self.head
        string_rep = ""
        while current:
            string_rep += f"{current} --> "
            current = current.next
        return string_rep

    def print_list(self):  # print every node data
        temp = self.head
        while temp:
            print(temp.item)
            temp = temp.next

def main():
    A = LinkedList()
    A.insert_head(input("Inserting 1st at head ").strip())
    A.insert_head(input("Inserting 2nd at head ").strip())
    print("\nPrint list:")
    A.print_list()
    A.insert_tail(input("\nInserting 1st at tail ").strip())
    A.insert_tail(input("Inserting 2nd at tail ").strip())
    print("\nPrint list:")
    A.print_list()
    print(A)
    print("\nDelete head")
    A.delete_head()
    print("Delete tail")
    A.delete_tail()
    print("\nPrint list:")
    A.print_list()
    print("\nReverse linked list")
    A.reverse()
    print("\nPrint list:")
    A.print_list()
    print("\nString representation of linked list:")
    print(A)
    print("\nReading/changing Node data using indexing:")
    print("New list:")
    print(A)


if __name__ == "__main__":
    main()



"""Interview question for SDET candidates"""

# QUESTION
# Given the following code, write a solution to print out the values of the linked list in reverse order.
# You are allowed to change any of the code we have provided if it will help in your solution.
# You are allowed to use a search engine as long as you don't search for the solution.

class Node:
    """Class Node."""
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_value(self) -> int:
        """Returns the value of the node."""
        return self.data

    def assign_next(self, data):
        """Points current node to a new node."""
        self.next = Node(data)


class LinkedList:
    """Class LinkedList."""
    def __init__(self, value):
        self.head = Node(value)

    def get_head(self)->Node:
        """Returns first node."""
        return self.head

    def append(self, value):
        """Appends a node to the tail of a linked list."""
        index_node = self.head
        while index_node.next is not None:
            index_node = index_node.next
        index_node.next = Node(value)

    def pop(self):
        """Removes a node from the tail of a linked list."""
        index_node = self.head
        while index_node.next.next is not None:
            index_node = index_node.next
        popped_node = index_node.next
        index_node.next = None
        return popped_node

    def size(self) -> str:
        """Returns the size of the linked list."""
        index_node = self.head
        count = 0
        while index_node is not None:
            count+=1
            index_node = index_node.next
        return count

    def print(self):
        """Prints the linked list."""
        index_node = self.head
        while index_node.next is not None:
            print(index_node.get_value())
            index_node = index_node.next



def main():
    """Main method. Populates linked list."""
    l_list = LinkedList(1)
    l_list.append(2)
    l_list.append(3)
    l_list.append(4)
    l_list.append(5)


main()

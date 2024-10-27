class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Додавання елемента в кінець списку
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Реверсування однозв'язного списку
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Сортування вставками для однозв'язного списку
    def sorted_insert(self, new_node):
        if not self.head or self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def insertion_sort(self):
        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            current.next = None
            if not sorted_list:
                sorted_list = current
            else:
                if sorted_list.data >= current.data:
                    current.next = sorted_list
                    sorted_list = current
                else:
                    temp = sorted_list
                    while temp.next and temp.next.data < current.data:
                        temp = temp.next
                    current.next = temp.next
                    temp.next = current
            current = next_node
        self.head = sorted_list

    # Об'єднання двох відсортованих однозв'язних списків
    @staticmethod
    def merge_sorted_lists(list1, list2):
        dummy = Node(0)
        tail = dummy
        a = list1.head
        b = list2.head

        while a and b:
            if a.data <= b.data:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        if a:
            tail.next = a
        if b:
            tail.next = b

        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list

    # Виведення списку
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Приклад використання
if __name__ == "__main__":
    # Створення списку та додавання елементів
    ll = LinkedList()
    ll.append(3)
    ll.append(1)
    ll.append(4)
    ll.append(2)

    print("Початковий список:")
    ll.print_list()

    # Реверсування списку
    ll.reverse()
    print("Реверсований список:")
    ll.print_list()

    # Сортування списку
    ll.insertion_sort()
    print("Відсортований список:")
    ll.print_list()

    # Об'єднання двох відсортованих списків
    ll1 = LinkedList()
    ll1.append(1)
    ll1.append(3)
    ll1.append(5)

    ll2 = LinkedList()
    ll2.append(2)
    ll2.append(4)
    ll2.append(6)

    merged_list = LinkedList.merge_sorted_lists(ll1, ll2)
    print("Об'єднаний відсортований список:")
    merged_list.print_list()

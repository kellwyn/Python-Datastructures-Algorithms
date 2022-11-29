# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 20:28:48 2022

@author: kellw
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, init_list=None):
        self.head = None
        if init_list:
            for value in init_list:
                self.append(value)
    
    def append(self,value):
        if self.head is None:
            self.head = Node(value)
        new_node = self.head
        while new_node.next:
            new_node = new_node.next
        new_node.next = Node(value)
        return self.head.value, new_node.next.value
    
    def prepend(self,value):
        if self.head is None:
            self.head = Node(value)

        prev_node = Node(value)
        prev_node.next = self.head
        self.head = prev_node                                      
        return self.head.value, prev_node.value, self.head.next.value,prev_node.next.value
    
    


linked_list = LinkedList()
print(linked_list.append(10))
print(linked_list.append(20))
print(linked_list.append(30))

print(linked_list.prepend(1))
print(linked_list.prepend(2))
print(linked_list.prepend(3))

list_with_loop = LinkedList([2, -1, 3, 0, 5])
list_with_loop1 = LinkedList([2, -1])
list_with_loop2 = LinkedList([3, 0, 5])

loop_start = list_with_loop.head.next

new_node = list_with_loop.head
while new_node.next:
    new_node = new_node.next
new_node.next = loop_start


new_node2 = list_with_loop2.head
while new_node2.next:
    new_node2 = new_node2.next
new_node2.next = list_with_loop2.head.next

def iscircular(linked_list):
    if linked_list.head is None:
        return False
    
    slow = linked_list.head
    fast = linked_list.head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    return False

small_loop = LinkedList([0])
small_loop.head.next = small_loop.head


print(iscircular(list_with_loop))
print(iscircular(list_with_loop1))
print(iscircular(list_with_loop2))
print(iscircular(small_loop))























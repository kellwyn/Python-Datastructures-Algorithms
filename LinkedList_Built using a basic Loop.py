# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 17:34:26 2022

@author: kellw
"""

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
   # def __repr__(self):
    #    return "Node()"
head = Node(2)
second_node = Node(1)
head.next = second_node
third_node = Node(6)
fourth_node = Node(8)
head.next.next = third_node
head.next.next.next = fourth_node


def print_linked_list(head):
    current_node = head
    while current_node is not None:
        print(current_node.value)
        current_node = current_node.next
        
        
    
print_linked_list(head)
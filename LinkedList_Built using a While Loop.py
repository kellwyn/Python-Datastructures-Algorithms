# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 20:34:42 2022

@author: kellw
"""


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
def create_linked_list(input_list):
    head = None
    
    for value in input_list:
        if head is None:
            head = Node(value)
        else:
            current_node = head
            while current_node.next:
                current_node = current_node.next
            current_node.next = Node(value)
    return head.value, current_node.value,current_node.next.value

input_list = [1,2,3,4,7,5,6]
print(create_linked_list(input_list))
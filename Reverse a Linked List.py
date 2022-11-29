# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 18:46:06 2022

@author: kellw
"""

# Helper Code

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        
    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next
            
    def __repr__(self):
        return str([v for v in self])
    

def reverse(linked_list):
    """
    Reverse the inputted linked list

    Args:
       linked_list(obj): Linked List to be reversed
    Returns:
       obj: Reveresed Linked List
    """
    
    # TODO: Write your function to reverse linked lists here
    
    new_list = LinkedList()
    
    
    prev_node = None
    next_node = None
    
    for value in linked_list:
        next_node = Node(value)
        next_node.next = prev_node
        prev_node = next_node
    
    new_list.head = prev_node
    
    return new_list
    
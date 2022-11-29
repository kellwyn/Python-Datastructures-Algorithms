# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 03:47:34 2022

@author: kellw
"""

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
   # def __repr__(self):
    #    return "Node()"
        

def create_linked_list_better(input_list):
    head = None
    tail = None
    
    for value in input_list:
        if head is None:
            head = Node(value)
            tail = head
            
        else:
            print(head.value)
            print("tail",tail.value)
            tail.next = Node(value)
            tail = tail.next
    return head, head.value, tail, tail.value
            


inputlist = [1,2,3,4,5,6,7]

print(create_linked_list_better(inputlist))
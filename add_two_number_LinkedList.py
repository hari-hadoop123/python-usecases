# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 06:33:58 2019

@author: Hari Chukkala
"""
# Description of the Problem: 

#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#Example:

#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8
#Explanation: 342 + 465 = 807.



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def get_digit(number, n):
        return number // 10**n % 10
    

    def stringToIntegerList(input):
        return json.loads(input)
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        factor=1 
        left_num=0 
        right_num=0
        left_node=l1
        right_node=l2
        while(True):
            if not left_node:
                break
            left_num=left_node.val*factor+left_num
            left_node=left_node.next
            factor=factor*10
        factor=1
        while(True):
            if not right_node:
                break
            right_num=right_node.val*factor+right_num
            right_node=right_node.next
            factor=factor*10

        total=left_num+right_num

        dummyRoot=ListNode(0)
        if (total==0):
            return dummyRoot
        result=dummyRoot
        
        for i in str(total)[::-1]:
            result.next=ListNode(i)
            result=result.next
        result=dummyRoot.next
        return result
 
            
            
            
            
            
        
            
        
        
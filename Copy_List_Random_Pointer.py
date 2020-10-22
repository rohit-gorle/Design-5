# Time - O(3N)
# Space - O(1)
# first creating a deep copy node next to the current node and in second pass updating the random pointers and in 3rd pass separating two lists and returning the deep copy list


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        if head == None:
            return None
        
        # Creating new deep copies next to current nodes 1-1'-2-2'-3-3'
        curr = head
        while curr != None:
            
            currCopy = Node(copy.deepcopy(curr.val))
            currCopy.next = curr.next
            curr.next = currCopy
            
            #advancing   
            curr = currCopy.next
        
        curr = head
        
        # random pointers assignment
        while curr != None:
            if curr.random != None:
                curr.next.random = curr.random.next
            
            else:
                curr.next.random = None
            curr = curr.next.next
        
        
        # creating 2 seperate lists 
        result = head.next
        oldList = head
        newList = head.next
        
        while oldList != None:
            oldList.next = oldList.next.next
            
            if newList.next != None:
                newList.next = newList.next.next
            else:
                newList.next = None
            
            oldList = oldList.next
            newList = newList.next
            
        return result
         

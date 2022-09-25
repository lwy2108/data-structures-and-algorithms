"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""


def linked_list_reverse(head):
  new_head = SinglyLinkedNode()
  curr = None
  while head.next:
    new_head.next = SinglyLinkedNode(head.val, curr)
    curr = new_head.next
    head = head.next
  new_head.val = head.val
  return new_head
  
  
def linked_list_reverse(head):
  def reverse_nodes(curr, prev):
    if curr is None:
      return prev
    else:
      next = curr.next
      curr.next = prev
      return reverse_nodes(next, curr)

  return reverse_nodes(head, None)


# test cases

class SinglyLinkedNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

        
head1 = SinglyLinkedNode(1, SinglyLinkedNode(2))
head2 = SinglyLinkedNode(1, SinglyLinkedNode(2, SinglyLinkedNode(3, SinglyLinkedNode(4, SinglyLinkedNode(5)))))

                         
def linked_list_to_list(head):
  vals = []
  curr = head
  while curr.val:
    vals.append(curr.val)
    curr = curr.next
    if not curr.next:
      vals.append(curr.val)
      break
  return vals


print(linked_list_to_list(head1), "Pass" if linked_list_to_list(linked_list_reverse(head1)) == [2, 1] else "Fail")
print(linked_list_to_list(head2), "Pass" if linked_list_to_list(linked_list_reverse(head2)) == [5, 4, 3, 2, 1] else "Fail")

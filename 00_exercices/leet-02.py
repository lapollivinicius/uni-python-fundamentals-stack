class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

l1 = ListNode([9,9,9,9,9,9,9], None)
l2 = ListNode([9,9,9,9], None)
l1.next = l2

def addTwoNumbers(l1, l2):
  l3 = ListNode()
  l3.val = [l1.val[i] + l2.val[i] for i in range(len(l1.val))]
  return l3.val

print(addTwoNumbers(l1, l2))
        